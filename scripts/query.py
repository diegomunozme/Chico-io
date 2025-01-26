import logging
import chromadb
from chromadb.config import Settings
from ollama import Client
# import scripts.config as config
import config
import sys

from pathlib import Path
import logging

# Define the path to the logs directory relative to this script
log_dir = Path(__file__).parent.parent / "logs"
log_dir.mkdir(parents=True, exist_ok=True)

# Define the log file path
log_file = log_dir / "application.log"

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create a file handler
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.INFO)

# Create a formatter and set it for the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Initialize the Ollama client
try:
    ollama_client = Client(host=config.OLLAMA_SERVER_URL)
    logger.info("Initialized Ollama client successfully.")
except Exception as e:
    logger.critical(f"Failed to initialize Ollama client: {e}")
    raise e

# Initialize ChromaDB Client
try:
    chroma_client = chromadb.PersistentClient(path=config.CHROMA_PATH)
    logger.info("Initialized Chroma client successfully.")
    db = chroma_client.get_collection(name=config.CHROMA_COLLECTION_NAME)
except chromadb.errors.InvalidCollectionException:
    logger.error(f"Collection '{config.CHROMA_COLLECTION_NAME}' does not exist.")
    raise
except Exception as e:
    logger.critical(f"Failed to initialize Chroma client: {e}")
    raise e

def embed_query(query: str) -> list:
    """
    Embed the user query using the Ollama embedding model.
    """
    try:
        response = ollama_client.embed(model=config.OLLAMA_EMBED_MODEL, input=query)
        if isinstance(response.get("embeddings"), list) and len(response["embeddings"]) > 0:
            embedding = response["embeddings"][0] if isinstance(response["embeddings"][0], list) else response["embeddings"]
            logger.debug("Successfully generated embedding for the query.")
            return embedding
        else:
            logger.error(f"Invalid embedding structure for the query: {response.get('embeddings')}")
            return None
    except Exception as e:
        logger.error(f"Error embedding the query: {e}")
        return None

def retrieve_relevant_chunks(query_embedding: list, top_k: int = 5) -> list:
    """
    Retrieve the top_k most similar document chunks from ChromaDB based on the query embedding.
    """
    try:
        results = db.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
            # include_metadata=True,
            # include_embeddings=False
        )
        retrieved_chunks = []
        for doc in results['documents'][0]:
            retrieved_chunks.append(doc)
        logger.info(f"Retrieved {len(retrieved_chunks)} relevant chunks.")
        return retrieved_chunks
    except Exception as e:
        logger.error(f"Error retrieving chunks from ChromaDB: {e}")
        return []

def generate_response(user_query: str, context_chunks: list) -> str:
    """
    Generate a response using the Ollama LLM model based on the user query and retrieved context.
    """
    try:
        # Combine the context chunks into a single context string
        context = "\n\n".join(context_chunks)
        
        # Construct the prompt
        prompt = (
            f"Context:\n{context}\n\n"
            f"Question: {user_query}\n"
            f"Answer:"
        )
        
        # Generate the response using Ollama LLM
        response = ollama_client.generate(
            model=config.OLLAMA_LLM_MODEL,
            prompt=prompt,
            # max_tokens=500,
            # temperature=0.7
        )
        
        if 'response' in response:
            logger.info("Successfully generated response from Ollama LLM.")
            return response['response']
        else:
            logger.error(f"Invalid response structure from LLM: {response}")
            return "I'm sorry, I couldn't generate a response at this time."
    except Exception as e:
        logger.error(f"Error generating response with Ollama LLM: {e}")
        return "I'm sorry, an error occurred while generating the response."

def main():
    if len(sys.argv) < 2:
        print("Usage: python rag_application.py 'Your query here'")
        sys.exit(1)
    
    user_query = sys.argv[1]
    logger.info(f"Received user query: {user_query}")
    
    # Step 1: Embed the query
    query_embedding = embed_query(user_query)
    if not query_embedding:
        print("Failed to embed the query. Check logs for details.")
        sys.exit(1)
    
    # Step 2: Retrieve relevant chunks
    relevant_chunks = retrieve_relevant_chunks(query_embedding, top_k=5)
    if not relevant_chunks:
        print("No relevant information found.")
        sys.exit(0)
    
    # Step 3: Generate response
    response = generate_response(user_query, relevant_chunks)
    print(f"Response: {response}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.critical(f"Application terminated due to an unhandled exception: {e}")
        sys.exit(1)
