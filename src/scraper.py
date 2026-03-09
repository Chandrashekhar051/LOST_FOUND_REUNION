import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://webscraper.io"
start_url = "https://webscraper.io/test-sites/e-commerce/static"

products = []

categories = [
"/computers/laptops",
"/computers/tablets",
"/phones/touch"
]

for category in categories:

    page = 1

    while True:

        url = f"{base_url}/test-sites/e-commerce/static{category}?page={page}"

        response = requests.get(url)

        soup = BeautifulSoup(response.text, "html.parser")

        items = soup.select(".thumbnail")

        if len(items) == 0:
            break

        for item in items:

            name = item.select_one(".title").text.strip()
            price = item.select_one(".price").text.strip()
            description = item.select_one(".description").text.strip()
            image = item.select_one("img")["src"]

            products.append({
                "product_name": name,
                "price": price,
                "description": description,
                "image_url": base_url + image
            })

        page += 1


df = pd.DataFrame(products)

df = df.drop_duplicates()

df.to_csv("data/scraped_products.csv", index=False)

print("Products scraped:", len(df))