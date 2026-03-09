import pandas as pd
import requests
import os

df=pd.read_csv("data/scraped_products.csv")

os.makedirs("images",exist_ok=True)

for i,row in df.iterrows():

    url=row["image_url"]

    for j in range(4):

        img=requests.get(url).content

        with open(f"images/product_{i}_{j}.jpg","wb") as f:
            f.write(img)