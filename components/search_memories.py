import streamlit as st
from utils import search_memories

def render_search_memories():
    st.markdown('<div class="section-header">Search Your Memories</div>', unsafe_allow_html=True)
    with st.container():
        query_text = st.text_input("Enter your search query:", placeholder="What are you looking for?")
        col1, col2 = st.columns([1, 5])
        with col1:
            search_button = st.button("🔎 Search", use_container_width=True)

        if search_button:
            if query_text.strip():
                with st.spinner("Searching memories..."):
                    response = search_memories(query_text, top_k=5)
                if response.status_code == 200:
                    data = response.json()
                    contexts = data.get("context", [])
                    if contexts:
                        st.markdown("### 📋 Found Memories:")
                        for i, doc in enumerate(contexts, 1):
                            st.markdown(f'<div class="memory-card"><strong>{i}.</strong> {doc}</div>', unsafe_allow_html=True)
                    else:
                        st.info("ℹ️ No matching memories found. Try a different query.")
                else:
                    st.error("❌ Search failed. Please check your connection.")
            else:
                st.warning("⚠️ Please enter a search query.")