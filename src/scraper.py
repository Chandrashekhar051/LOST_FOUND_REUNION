import os
import random
import pandas as pd
from PIL import Image, ImageDraw, ImageFont

os.makedirs("images", exist_ok=True)
os.makedirs("data", exist_ok=True)

brands = [
    "Apple","Samsung","Sony","JBL","Bose",
    "Casio","Rolex","Fossil","Boat","Noise"
]

products = [
    "watch",
    "phone",
    "headphones",
    "earbuds",
    "phone case",
    "laptop",
    "tablet"
]

colors = [
    "black","white","silver","gold",
    "blue","pink","red","green"
]

font = ImageFont.load_default()


def draw_watch(draw,color):
    draw.rectangle((110,20,146,236),fill=color)
    draw.ellipse((80,90,176,186),fill=(240,240,240))


def draw_phone(draw,color):
    draw.rectangle((90,40,166,216),fill=color)


def draw_headphones(draw,color):
    draw.arc((60,20,196,140),0,180,fill=color,width=8)
    draw.rectangle((60,120,100,180),fill=color)
    draw.rectangle((156,120,196,180),fill=color)


def draw_earbuds(draw,color):
    draw.ellipse((90,100,120,130),fill=color)
    draw.ellipse((140,100,170,130),fill=color)


def draw_case(draw,color):
    draw.rectangle((90,40,166,216),outline=color,width=8)


def draw_laptop(draw,color):
    draw.rectangle((70,70,186,150),fill=color)
    draw.rectangle((60,150,196,170),fill=(150,150,150))


def draw_tablet(draw,color):
    draw.rectangle((80,40,176,216),fill=color)


def generate_image(product,name,color,index,img_id):

    img = Image.new("RGB",(256,256),(250,250,250))
    draw = ImageDraw.Draw(img)

    if product == "watch":
        draw_watch(draw,color)

    elif product == "phone":
        draw_phone(draw,color)

    elif product == "headphones":
        draw_headphones(draw,color)

    elif product == "earbuds":
        draw_earbuds(draw,color)

    elif product == "phone case":
        draw_case(draw,color)

    elif product == "laptop":
        draw_laptop(draw,color)

    elif product == "tablet":
        draw_tablet(draw,color)

    draw.text((20,10),name,fill=(0,0,0),font=font)

    path = f"images/product_{index}_{img_id}.jpg"

    img.save(path)


rows = []

for i in range(100):

    brand = random.choice(brands)
    product = random.choice(products)
    color_name = random.choice(colors)

    name = f"{brand} {color_name} {product}"

    description = f"{color_name} {product} from {brand}"

    color_map = {
        "black":(40,40,40),
        "white":(230,230,230),
        "silver":(180,180,180),
        "gold":(212,175,55),
        "blue":(80,120,255),
        "pink":(255,140,200),
        "red":(220,50,50),
        "green":(60,180,90)
    }

    color = color_map[color_name]

    rows.append({
        "product_name": name,
        "price": "$100",
        "description": description
    })

    for j in range(2):

        generate_image(product,name,color,i,j)

df = pd.DataFrame(rows)

df.to_csv("data/scraped_products.csv", index=False)

print("Generated 100 products and 200 images")
