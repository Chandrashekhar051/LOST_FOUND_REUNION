import streamlit as st
from src.search_engine import search
from src.explain_results import explain

st.title("Lost & Found Reunion 🔍")

st.write("Search for your lost item using a description.")

query = st.text_input("Describe your lost item")

if st.button("Search"):

    if query.strip() == "":
        st.warning("Please enter a description.")
    else:

        results = search(query)

        docs = results["documents"][0]
        scores = results["distances"][0]
        metas = results["metadatas"][0]

        st.subheader("Matching Items")

        for doc, score, meta in zip(docs, scores, metas):

            confidence = 1 / (1 + score)

            st.write("### Match:", meta["product"])
            st.write("Category:", meta["category"])
            st.write("Confidence:", round(confidence, 2))

            image_path = meta["image"]

            st.image(image_path, width=200)

            explanation = explain(query, meta["product"])

            st.write("AI Explanation:")
            st.write(explanation)

            st.write("---")
