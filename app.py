import streamlit as st
from src.search_engine import search
from PIL import Image
import tempfile

st.title("🔍 Lost & Found Reunion")

st.write("Search using description or upload image")

query = st.text_input("Describe your lost item")

uploaded_file = st.file_uploader("Upload image of lost item", type=["jpg","png","jpeg"])

if st.button("Search"):

    if query == "" and uploaded_file is None:
        st.warning("Enter description or upload image")
    else:

        if uploaded_file is not None:

            image = Image.open(uploaded_file)

            st.image(image, caption="Uploaded Image", width=200)

            query = "electronic device"

        results = search(query)

        docs = results["documents"][0]
        scores = results["distances"][0]
        metas = results["metadatas"][0]

        st.subheader("Matching Items")

        for doc, score, meta in zip(docs, scores, metas):

            confidence = 1/(1+score)

            st.write("### Match:", meta["product"])
            st.write("Category:", meta["category"])
            st.write("Confidence:", round(confidence,2))

            st.image(meta["image"], width=200)

            st.write("---")
