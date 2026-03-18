import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection(name="lost_items")

model = SentenceTransformer("all-MiniLM-L6-v2")


# keywords used in dataset
colors = [
    "black","white","silver","gold",
    "blue","pink","red","green"
]

brands = [
    "apple","samsung","sony","rolex",
    "casio","fossil","jbl","boat",
    "noise","bose"
]

products = [
    "watch","phone","laptop","tablet",
    "headphones","earbuds","case"
]


# simple typo correction
typo_map = {
    "fone":"phone",
    "fonecase":"phone case",
    "hedphones":"headphones",
    "earbud":"earbuds",
    "earbudz":"earbuds",
    "loptop":"laptop",
    "wotch":"watch"
}


def correct_typos(query):

    words = query.lower().split()

    corrected = []

    for w in words:

        if w in typo_map:
            corrected.append(typo_map[w])
        else:
            corrected.append(w)

    return " ".join(corrected)


def expand_query(query):

    q = query.lower()

    tokens = [q]

    for color in colors:
        if color in q:
            tokens.append(color)

    for brand in brands:
        if brand in q:
            tokens.append(brand)

    for product in products:
        if product in q:
            tokens.append(product)

    return " ".join(tokens)


# boost important words
def boost_keywords(query):

    words = query.split()

    boosted = words + words

    return " ".join(boosted)


def search(query):

    # typo correction
    query = correct_typos(query)

    # expand query
    expanded_query = expand_query(query)

    # boost important words
    boosted_query = boost_keywords(expanded_query)

    query_embedding = model.encode(boosted_query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=20
    )

    docs = results["documents"][0]
    metas = results["metadatas"][0]
    distances = results["distances"][0]

    seen = set()

    filtered_docs = []
    filtered_meta = []
    filtered_dist = []

    for doc, meta, dist in zip(docs, metas, distances):

        product = meta["product"]

        if product not in seen:

            seen.add(product)

            filtered_docs.append(doc)
            filtered_meta.append(meta)
            filtered_dist.append(dist)

        if len(filtered_docs) == 4:
            break

    return {
        "documents":[filtered_docs],
        "metadatas":[filtered_meta],
        "distances":[filtered_dist]
    }
