from sentence_transformers import SentenceTransformer
import pandas as pd
import pickle

model=SentenceTransformer("all-MiniLM-L6-v2")

df=pd.read_csv("data/lost_found_dataset_cleaned.csv")

embeddings=model.encode(df["searchable_text"].tolist())

with open("embeddings/text_embeddings.pkl","wb") as f:
    pickle.dump(embeddings,f)