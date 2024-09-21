import chromadb
from chromadb import Documents, EmbeddingFunction, Embeddings
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

class GeminiEmbeddingFunction(EmbeddingFunction):
    def __init__(self):
        self.api_key = os.getenv('GEMINI_API_KEY')
        genai.configure(api_key=self.api_key)

    def __call__(self, input: Documents) -> Embeddings:
        model = 'models/embedding-001'
        title = "Custom query"
        embeddings = genai.embed_content(model=model,
                                         content=input,
                                         task_type="retrieval_document",
                                         title=title)["embedding"]
        return embeddings

def create_chroma_db(name):
    chroma_client = chromadb.Client()
    embedding_function = GeminiEmbeddingFunction()
    
    # Ensure the collection is created afresh every session
    if name in [collection.name for collection in chroma_client.list_collections()]:
        chroma_client.delete_collection(name)
    db = chroma_client.create_collection(name=name, embedding_function=embedding_function)

    return db

def add_documents_to_db(db, documents):
    for i, d in enumerate(documents):
        db.add(
            documents=d,
            ids=str(i)
        )
    # Log the documents added to the database
    print(f"Documents added to the database: {documents}")

def get_relevant_passage(query, db):
    results = db.query(query_texts=[query], n_results=1)
    print(f"Query results: {results}")  # Log the results of the query
    if results['documents'] and results['documents'][0]:
        passage = results['documents'][0][0]
    else:
        passage = None
    return passage

def peek_db(db, n=2):
    return db.peek(n)
