import chromadb
from sentence_transformers import SentenceTransformer

# connect to persistent database
client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection(name="lost_items")

model = SentenceTransformer("all-MiniLM-L6-v2")

def search(query):

    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=5
    )

    return results