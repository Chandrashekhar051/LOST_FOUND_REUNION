import pandas as pd
import os

df = pd.read_csv("data/scraped_products.csv")

df = df.drop_duplicates()
df = df.dropna()


def category(name):

    name = name.lower()

    if "watch" in name:
        return "watch"

    if "phone case" in name:
        return "case"

    if "phone" in name:
        return "phone"

    if "laptop" in name:
        return "laptop"

    if "tablet" in name:
        return "tablet"

    if "headphone" in name:
        return "headphones"

    if "earbud" in name:
        return "earbuds"

    return "electronics"


df["category"] = df["product_name"].apply(category)


rows = []

for idx,row in df.iterrows():

    name = row["product_name"].lower()

    # extract brand and color from product name
    words = name.split()

    brand = words[0] if len(words) > 0 else ""
    color = words[1] if len(words) > 1 else ""

    for i in range(4):

        image_path = f"images/product_{idx}_{i}.jpg"

        if os.path.exists(image_path):

            new_row = row.copy()

            new_row["image_path"] = image_path

            new_row["searchable_text"] = (
                row["product_name"] + " " +
                row["description"] + " " +
                brand + " " +
                color + " " +
                new_row["category"]
            )

            rows.append(new_row)


df = pd.DataFrame(rows)

df.to_csv("data/lost_found_dataset_cleaned.csv", index=False)

print("Clean dataset created:", len(df))
