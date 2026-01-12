import streamlit as st
from utils import get_all_memories, delete_memory

def render_manage_memories():
    st.markdown('<div class="section-header">Manage Your Memories</div>', unsafe_allow_html=True)
    with st.container():
        if st.button("🔄 Refresh Memories"):
            st.rerun()

        response = get_all_memories()
        if response.status_code == 200:
            data = response.json()
            documents = data.get("documents", [])
            ids = data.get("ids", [])
            if documents and ids:
                st.markdown(f"### 📚 All Memories ({len(documents)} total)")
                for i, (doc, doc_id) in enumerate(zip(documents, ids), 1):
                    with st.expander(f"Memory {i}: {doc[:50]}..."):
                        st.write(doc)
                        col1, col2 = st.columns([4, 1])
                        with col2:
                            if st.button("🗑️ Delete", key=f"del-{doc_id}"):
                                with st.spinner("Deleting..."):
                                    del_res = delete_memory(doc_id)
                                if del_res.status_code == 200:
                                    st.success("✅ Memory deleted successfully!")
                                    st.rerun()
                                else:
                                    st.error("❌ Failed to delete memory.")
            else:
                st.info("ℹ️ No memories stored yet. Add some in the 'Add Memory' tab!")
        else:
            st.error("❌ Failed to fetch memories. Please check your connection.")