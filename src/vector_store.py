import chromadb
import pandas as pd
from sentence_transformers import SentenceTransformer

print("Loading dataset...")

df = pd.read_csv("data/lost_found_dataset_cleaned.csv")

print("Loading embedding model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

print("Creating embeddings...")

embeddings = model.encode(df["searchable_text"].tolist())

print("Connecting to Chroma persistent database...")

client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection(name="lost_items")

print("Storing vectors in database...")

collection.add(
    documents=df["searchable_text"].tolist(),
    embeddings=embeddings.tolist(),
    ids=[str(i) for i in range(len(df))],
    metadatas=[
        {
            "product": df.iloc[i]["product_name"],
            "image": df.iloc[i]["image_path"],
            "category": df.iloc[i]["category"]
        }
        for i in range(len(df))
    ]
)

print("✅ Database created successfully!")