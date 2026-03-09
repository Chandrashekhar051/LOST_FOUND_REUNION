# Lost & Found Reunion 🔍

### A Multi-Modal Semantic Search Engine for Lost Items

## Project Overview

Lost & Found departments often store hundreds of items with vague descriptions such as
"black bag", "electronics", or "found near canteen".

Traditional search systems cannot understand the meaning behind item descriptions.

**Lost & Found Reunion** is an AI-powered semantic search system that allows users to search lost items using natural language descriptions and retrieve the most relevant matches.

The system uses **Sentence Transformers**, **ChromaDB**, and a **Streamlit interface** to provide intelligent search results.

---

# Problem

Students frequently lose items such as phones, laptops, tablets, and headphones.

Lost & Found offices log items using vague descriptions, making it difficult to identify the correct owner.

Problems include:

* vague descriptions
* manual search through spreadsheets
* no image search
* items often get donated before the owner finds them

This project solves these issues using **AI semantic search**.

---

# Project Approach

The project follows an end-to-end AI pipeline.

### 1. Data Collection

Product data was scraped from an e-commerce test website using **BeautifulSoup**.

Collected fields:

* product_name
* description
* price
* image_url

Stored in:

```
data/scraped_products.csv
```

---

### 2. Dataset Generation

Realistic lost item descriptions were generated using templates.

Example:

```
"I lost my apple ipad air near the parking area."
```

These descriptions simulate real lost item reports.

---

### 3. Data Cleaning

Cleaning steps included:

* removing duplicates
* removing missing values
* assigning categories
* generating searchable text

Searchable text example:

```
product_name + description + lost_description + category
```

Clean dataset saved as:

```
data/lost_found_dataset_cleaned.csv
```

---

### 4. Text Embeddings

Text data was converted into vector embeddings using:

```
SentenceTransformer
Model: all-MiniLM-L6-v2
```

Embeddings capture the semantic meaning of descriptions.

---

### 5. Vector Database

Embeddings were stored in **ChromaDB**.

The vector database stores:

* embeddings
* product metadata
* image paths

This enables fast similarity search.

---

### 6. Semantic Search

When a user enters a query:

1. Query is converted into embedding
2. Vector similarity search is performed
3. Top matching results are returned
4. Confidence score is calculated

---

### 7. AI Explanation

A local LLM (**TinyLlama via Ollama**) explains why a particular item matches the query.

Example explanation:

```
The query refers to an iPad device. The matched item is Apple iPad Air,
which belongs to the tablet category and closely matches the description.
```

---

# Sample Search Results

### Example Query

```
ipad
```

### Result

```
Match: Apple iPad Air Wi-Fi 64GB
Confidence Score: 0.54
Category: Electronics
```

Another example:

```
Query: android tablet lost
```

```
Match: MeMo PAD FHD 10.1
Confidence Score: 0.50
```

---

# Technologies Used

Python           
Streamlit                
Sentence Transformers                  
ChromaDB                        
Ollama (TinyLlama)                  
BeautifulSoup                         
Pandas                               
Pillow                          

---

# Project Structure

```
lost-found-reunion
│
├── app.py
├── requirements.txt
├── README.md
│
├── data
│   ├── scraped_products.csv
│   └── lost_found_dataset_cleaned.csv
│
├── images
│
├── embeddings
│
├── chroma_db
│
└── src
    ├── scraper.py
    ├── generate_lost_descriptions.py
    ├── download_images.py
    ├── clean_dataset.py
    ├── create_embeddings.py
    ├── vector_store.py
    ├── search_engine.py
    └── explain_results.py
```

---

# How to Run the Project

Install dependencies

```
pip install -r requirements.txt
```

Run the Streamlit application

```
streamlit run app.py
```

---

# Future Improvements

If more development time was available, the following improvements could be implemented:

1. True multi-modal search using CLIP embeddings for both text and images.
2. Larger dataset scraped from real marketplaces.
3. Notification system when a matching item appears.
4. Mobile application for reporting lost items.
5. Integration with university lost-and-found systems.

---

# Conclusion

Lost & Found Reunion demonstrates how **AI semantic search and vector databases** can solve real-world problems by improving item matching and helping people recover lost belongings.
