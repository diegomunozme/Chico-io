import subprocess
import sys
import argparse

def populate_database():
    print("Populating the Chroma DB...")
    result = subprocess.run([sys.executable, "scripts/populate_database.py"], capture_output=True, text=True)
    if result.returncode != 0:
        print("Error populating database:", result.stderr)
        sys.exit(result.returncode)
    print("Database populated successfully.")

def query_database(prompt):
    print("Querying the Chroma DB with Ollama...")
    result = subprocess.run([sys.executable, "scripts/query.py", prompt], capture_output=True, text=True)
    if result.returncode != 0:
        print("Error querying database:", result.stderr)
        sys.exit(result.returncode)
    print("Query executed successfully.")
    print("Result:", result.stdout)

def main():
    parser = argparse.ArgumentParser(description="RAG Application")
    parser.add_argument(
        '--prompt',
        type=str,
        help='Prompt for the RAG query. Example: "What are the steps to make meatloaf according to diet cheat codes, answer like Chef Gordon Ramsay."'
    )
    args = parser.parse_args()

    # Use a default prompt if none is provided
    prompt = args.prompt or "What are the steps to make nickchicken according to diet cheat codes, answer like Chef Gordon Ramsay."

    populate_database()
    query_database(prompt)

if __name__ == "__main__":
    main()
