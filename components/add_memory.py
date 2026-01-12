import streamlit as st
from utils import add_memory

def render_add_memory():
    st.markdown('<div class="section-header">Add a New Memory</div>', unsafe_allow_html=True)
    with st.container():
        memory_text = st.text_area("Enter your memory or note:", height=150, placeholder="Write something meaningful to remember...")
        col1, col2, col3 = st.columns([1, 1, 3])
        with col1:
            add_button = st.button("➕ Add Memory", use_container_width=True)
        with col2:
            clear_button = st.button("🗑️ Clear", use_container_width=True)

        if clear_button:
            memory_text = ""
            st.rerun()

        if add_button:
            if memory_text.strip():
                with st.spinner("Storing memory..."):
                    response = add_memory(memory_text)
                if response.status_code == 200:
                    data = response.json()
                    st.success(f"✅ Memory stored successfully! ID: {data.get('id')}")
                    memory_text = ""
                else:
                    st.error("❌ Failed to store memory. Please try again.")
            else:
                st.warning("⚠️ Please enter some text before adding.")