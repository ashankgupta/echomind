import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.title("🧠 Personal Memory Embedding & Search")

# Add Memory Section
st.header("Add Memory")
memory_text = st.text_area("Write something to remember:")

if st.button("Add Memory"):
    if memory_text.strip():
        response = requests.post(f"{API_URL}/ingest", json={"text": memory_text})
        if response.status_code == 200:
            data = response.json()
            st.success(f"Memory stored with id: {data.get('id')}")
            memory_text = ""
        else:
            st.error("Failed to store memory!")
    else:
        st.warning("Please enter some text.")

st.markdown("---")

# Search Memory Section
st.header("Search Memories")
query_text = st.text_input("Enter your query:")

if st.button("Search"):
    if query_text.strip():
        response = requests.post(
            f"{API_URL}/context",
            json={"query": query_text, "top_k": 5},
        )
        if response.status_code == 200:
            data = response.json()
            contexts = data.get("context", [])
            if contexts:
                st.write("### Found Memories:")
                for i, doc in enumerate(contexts, 1):
                    st.write(f"{i}. {doc}")
            else:
                st.info("No matching memories found.")
        else:
            st.error("Search failed!")
    else:
        st.warning("Please enter a query.")

st.markdown("---")

# Show all stored memories with delete option
if st.checkbox("Show all stored memories"):
    response = requests.get(f"{API_URL}/all_memories")
    if response.status_code == 200:
        data = response.json()
        documents = data.get("documents", [])
        ids = data.get("ids", [])
        if documents and ids:
            st.write("### All Memories:")
            for i, (doc, doc_id) in enumerate(zip(documents, ids), 1):
                col1, col2 = st.columns([5, 1])
                with col1:
                    st.write(f"{i}. {doc}")
                with col2:
                    if st.button("❌", key=f"del-{doc_id}"):
                        del_res = requests.delete(f"{API_URL}/delete", json={"id": doc_id})
                        if del_res.status_code == 200:
                            st.success(f"Deleted: {doc}")
                            st.rerun()
                        else:
                            st.error("Delete failed.")
        else:
            st.info("No memories stored yet.")
    else:
        st.error("Failed to fetch memories.")


