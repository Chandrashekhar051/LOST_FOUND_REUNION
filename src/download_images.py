import pandas as pd
import os
import requests
import time
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO

df = pd.read_csv("data/scraped_products.csv")

os.makedirs("images", exist_ok=True)

headers = {"User-Agent": "Mozilla/5.0"}


def detect_product_type(name):

    name = name.lower()

    if "watch" in name:
        return "watch"

    if "phone case" in name or "case" in name:
        return "phone case"

    if "phone" in name:
        return "phone"

    if "headphones" in name:
        return "headphones"

    if "earbuds" in name:
        return "earbuds"

    if "laptop" in name:
        return "laptop"

    if "tablet" in name:
        return "tablet"

    return ""


def download_images(product_name, index):

    product_type = detect_product_type(product_name)

    query = f"{product_name} {product_type}"

    search_url = f"https://www.bing.com/images/search?q={query}"

    count = 0

    try:

        response = requests.get(search_url, headers=headers, timeout=10)

        soup = BeautifulSoup(response.text, "html.parser")

        images = soup.select("img")

        for img in images:

            if count == 2:
                break

            src = img.get("src")

            if not src or "http" not in src:
                continue

            try:

                r = requests.get(src, headers=headers, timeout=10)

                image = Image.open(BytesIO(r.content)).convert("RGB")

                image = image.resize((256,256))

                path = f"images/product_{index}_{count}.jpg"

                image.save(path,"JPEG",quality=70)

                print("Saved:", path)

                count += 1

            except:
                continue

    except Exception as e:

        print("Search failed:", product_name)


for i,row in df.iterrows():

    product = row["product_name"]

    print("\nDownloading images for:", product)

    download_images(product,i)

    time.sleep(1)


print("\nImages downloaded successfully")
