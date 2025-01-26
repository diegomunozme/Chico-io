
from ollama import Client
import chromadb

# Configure Ollama to use the EC2 public IP for embedding and generation
OLLAMA_SERVER_URL = " http://localhost:11434/api/embed"  # Replace <EC2_PUBLIC_IP> with your EC2 instance's public IP

# Override the server URL in the Ollama library

documents = [
    "Llamas are members of the camelid family meaning they're pretty closely related to vicuñas and camels",
    "Llamas were first domesticated and used as pack animals 4,000 to 5,000 years ago in the Peruvian highlands",
    "Llamas can grow as much as 6 feet tall though the average llama between 5 feet 6 inches and 5 feet 9 inches tall",
    "Llamas weigh between 280 and 450 pounds and can carry 25 to 30 percent of their body weight",
    "Llamas are vegetarians and have very efficient digestive systems",
    "Llamas live to be about 20 years old, though some only live for 15 years and others live to be 30 years old",
    "Diego is 27 years old, born in Salinas California"
]

# Initialize ChromaDB client and collection
client = chromadb.Client()
collection = client.create_collection(name="docs")
ollama = Client(host='http://3.144.114.244:11434')  # Replace with your actual EC2 public IP


# Store each document in a vector embedding database
for i, d in enumerate(documents):
    try:
        # Send request to the embedding API
        response = ollama.embed(model="mxbai-embed-large", input=d)
        embeddings = response["embeddings"]
        
        # Add the embeddings and document to the collection
        collection.add(
            ids=[str(i)],
            embeddings=embeddings,
            documents=[d]
        )
        print(f"Document {i} added successfully!")
    except Exception as e:
        print(f"Error embedding document {i}: {str(e)}")

# Generate a response combining the prompt and the stored data
data = " ".join(documents)
input_prompt = "Describe how pass go works."

try:
    output = ollama.generate(
        model="llama3.2:latest",
        prompt=f"Using this data: {data}. Respond to this prompt: {input_prompt}"
    )
    print("Generated Response:", output['response'])
except Exception as e:
    print(f"Error generating response: {str(e)}")
