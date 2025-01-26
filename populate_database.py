import argparse
import os
import shutil
import logging  # Import the logging module
from langchain_community.document_loaders import PyPDFDirectoryLoader  # Updated import based on previous warnings
from langchain.text_splitter import CharacterTextSplitter

from langchain.schema import Document
import chromadb
from chromadb.config import Settings  # Import Settings for explicit configuration
from ollama import Client
import config  # Import shared configuration

# Logging Configuration
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_LEVEL = logging.DEBUG  # Set to DEBUG for detailed logs during troubleshooting

logging.basicConfig(
    level=LOG_LEVEL,
    format=LOG_FORMAT,
    handlers=[
        logging.FileHandler("populate_database.log"),  # Log to a file
        logging.StreamHandler()  # Also log to console
    ]
)

logger = logging.getLogger(__name__)  # Create a logger for this module

# Initialize the Ollama client
try:
    ollama_client = Client(host=config.OLLAMA_SERVER_URL)
    logger.info("Initialized Ollama client successfully.")
except Exception as e:
    logger.critical(f"Failed to initialize Ollama client: {e}")
    raise e

# Initialize ChromaDB Client with explicit persist_directory
try:
    chroma_client = chromadb.PersistentClient(path=config.CHROMA_PATH
    )
    logger.info("Initialized Chroma client successfully.")
except Exception as e:
    logger.critical(f"Failed to initialize Chroma client: {e}")
    raise e

def main():
    # Check if the database should be cleared (using the --reset flag).
    parser = argparse.ArgumentParser(description="Populate ChromaDB with embedded PDF data.")
    parser.add_argument("--reset", action="store_true", help="Reset the database.")
    args = parser.parse_args()
    
    if args.reset:
        logger.info("Reset flag detected. Clearing the existing database.")
        clear_database()
    
    logger.info("Loading documents from PDF files.")
    documents = load_documents()
    logger.info(f"Loaded {len(documents)} documents.")
    
    logger.info("Splitting documents into chunks.")
    chunks = split_documents(documents)
    logger.info(f"Split documents into {len(chunks)} chunks.")
    
    logger.info("Adding chunks to ChromaDB.")
    add_to_chroma(chunks)
    logger.info("Completed adding chunks to ChromaDB.")

def load_documents():
    try:
        if not os.path.exists(config.DATA_PATH):
            logger.error(f"DATA_PATH '{config.DATA_PATH}' does not exist.")
            raise FileNotFoundError(f"DATA_PATH '{config.DATA_PATH}' does not exist.")
        
        document_loader = PyPDFDirectoryLoader(config.DATA_PATH)
        documents = document_loader.load()
        logger.debug(f"Loaded documents: {documents}")
        return documents
    except Exception as e:
        logger.error(f"Error loading documents: {e}")
        raise e

def split_documents(documents: list[Document]):
    try:
        if not documents:
            logger.warning("No documents to split.")
            return []
        
        text_splitter = CharacterTextSplitter(
            chunk_size=800,
            chunk_overlap=80,
            length_function=len,
            is_separator_regex=False,
        )
        chunks = text_splitter.split_documents(documents)
        logger.debug(f"Generated {len(chunks)} chunks from documents.")
        return chunks
    except Exception as e:
        logger.error(f"Error splitting documents: {e}")
        raise e

def get_ollama_embeddings(texts: list[str]):
    """
    Custom embedding function using the Ollama API for batch embeddings.
    """
    embeddings = []
    for idx, text in enumerate(texts):
        try:
            response = ollama_client.embed(model=config.OLLAMA_EMBED_MODEL, input=text)
            
            # Verify the structure of the embeddings
            if isinstance(response.get("embeddings"), list) and len(response["embeddings"]) > 0:
                # Extract the first embedding if it's nested
                embedding = response["embeddings"][0] if isinstance(response["embeddings"][0], list) else response["embeddings"]
                embeddings.append(embedding)
                logger.debug(f"Generated embedding for text index {idx}.")
            else:
                logger.error(f"Invalid embedding structure for text index {idx}: {response.get('embeddings')}")
                embeddings.append(None)
        except Exception as e:
            logger.error(f"Error embedding text at index {idx}: {e}")
            embeddings.append(None)  # Add None for failed embeddings
    return embeddings

def add_to_chroma(chunks: list[Document]):
    try:
        # Load or create the 'data' collection
        try:
            db = chroma_client.get_collection(name=config.CHROMA_COLLECTION_NAME)
            logger.info(f"Accessed the '{config.CHROMA_COLLECTION_NAME}' collection in ChromaDB.")
        except chromadb.errors.InvalidCollectionException:
            logger.info(f"Collection '{config.CHROMA_COLLECTION_NAME}' does not exist. Creating it.")
            db = chroma_client.create_collection(
                name=config.CHROMA_COLLECTION_NAME,
                embedding_function=None  # Custom embedding function is used
            )
            logger.info(f"Created the '{config.CHROMA_COLLECTION_NAME}' collection in ChromaDB.")
        except Exception as e:
            logger.critical(f"Failed to access or create ChromaDB collection: {e}")
            raise e

        # Calculate Chunk IDs
        chunks_with_ids = calculate_chunk_ids(chunks)
        logger.debug("Calculated unique IDs for each chunk.")
        
        # Extract texts from chunks
        texts = [chunk.page_content for chunk in chunks_with_ids]
        logger.debug("Extracted texts from chunks.")
        
        # Generate embeddings using Ollama
        logger.info("Generating embeddings for the chunks.")
        embeddings = get_ollama_embeddings(texts)
        logger.info("Completed generating embeddings.")
        
        # Filter out chunks with failed embeddings
        valid_chunks = []
        valid_embeddings = []
        valid_ids = []
        for chunk, embedding in zip(chunks_with_ids, embeddings):
            if embedding is not None:
                valid_chunks.append(chunk)
                valid_embeddings.append(embedding)
                valid_ids.append(chunk.metadata["id"])
            else:
                logger.warning(f"Skipping chunk ID {chunk.metadata['id']} due to failed embedding.")
        
        # Prepare documents for upsert
        documents = [chunk.page_content for chunk in valid_chunks]
        
        # Add new documents to Chroma
        if valid_chunks:
            logger.info(f"Upserting {len(valid_chunks)} documents into ChromaDB.")
            try:
                db.upsert(
                    documents=documents,  # The actual texts
                    embeddings=valid_embeddings,  # The embeddings
                    ids=valid_ids  # The IDs
                )
                logger.info(f"Successfully upserted {len(valid_chunks)} documents.")
            except Exception as e:
                logger.error(f"Failed to upsert documents to ChromaDB: {e}")
                raise e
        else:
            logger.info("No valid documents to upsert.")
    except Exception as e:
        logger.error(f"An error occurred while adding chunks to ChromaDB: {e}")
        raise e

def calculate_chunk_ids(chunks):
    # This will create IDs like "data/monopoly.pdf:6:2"
    # Page Source : Page Number : Chunk Index

    last_page_id = None
    current_chunk_index = 0

    for chunk in chunks:
        source = chunk.metadata.get("source")
        page = chunk.metadata.get("page")
        current_page_id = f"{source}:{page}"

        # If the page ID is the same as the last one, increment the index.
        if current_page_id == last_page_id:
            current_chunk_index += 1
        else:
            current_chunk_index = 0

        # Calculate the chunk ID.
        chunk_id = f"{current_page_id}:{current_chunk_index}"
        last_page_id = current_page_id

        # Add it to the page meta-data.
        chunk.metadata["id"] = chunk_id
        logger.debug(f"Assigned ID {chunk_id} to chunk.")

    return chunks

def clear_database():
    try:
        if os.path.exists(config.CHROMA_PATH):
            shutil.rmtree(config.CHROMA_PATH)
            logger.info(f"Cleared the ChromaDB at path: {config.CHROMA_PATH}")
        else:
            logger.warning(f"ChromaDB path '{config.CHROMA_PATH}' does not exist. Nothing to clear.")
    except Exception as e:
        logger.error(f"Failed to clear the database: {e}")
        raise e

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.critical(f"Script terminated due to an unhandled exception: {e}")
