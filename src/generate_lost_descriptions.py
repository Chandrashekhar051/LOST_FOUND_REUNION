import pandas as pd
import random

df = pd.read_csv("data/scraped_products.csv")

templates = [
"I lost my {item} near the bus stop yesterday evening.",
"My {item} went missing near the campus cafeteria.",
"I misplaced my {item} somewhere in the library.",
"I dropped my {item} near the parking area.",
"A {item} was reported missing near the main gate.",
"I think I left my {item} in the lecture hall.",
"Someone might have seen a {item} near the hostel area.",
"I lost my {item} while commuting this morning."
]

lost_reports = []

for name in df["product_name"]:

    item = name.lower()
    sentence = random.choice(templates).format(item=item)

    lost_reports.append(sentence)

df["lost_description"] = lost_reports

df.to_csv("data/scraped_products.csv", index=False)

print("Lost descriptions generated:", len(df))