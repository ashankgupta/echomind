import streamlit as st
from components.add_memory import render_add_memory
from components.search_memories import render_search_memories
from components.manage_memories import render_manage_memories
from utils import check_api_status

st.set_page_config(
    page_title="EchoMind - Personal Memory Assistant",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    .section-header {
        font-size: 1.5rem;
        font-weight: 600;
        color: #2c3e50;
        margin-top: 1rem;
        margin-bottom: 1rem;
        border-bottom: 2px solid #1f77b4;
        padding-bottom: 0.5rem;
    }
    .memory-card {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 0.5rem 0;
        border-left: 5px solid #1f77b4;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: transform 0.2s;
    }
    .memory-card:hover {
        transform: translateY(-2px);
    }
    .stButton>button {
        background: linear-gradient(135deg, #1f77b4 0%, #155a8a 100%);
        color: white;
        border-radius: 8px;
        border: none;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #155a8a 0%, #0d3a5c 100%);
        transform: scale(1.05);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    .stTextInput>div>div>input, .stTextArea>div>textarea {
        border-radius: 8px;
        border: 2px solid #ddd;
        padding: 0.75rem;
        font-size: 1rem;
        transition: border-color 0.3s;
    }
    .stTextInput>div>div>input:focus, .stTextArea>div>textarea:focus {
        border-color: #1f77b4;
        box-shadow: 0 0 0 2px rgba(31, 119, 180, 0.2);
    }
    .sidebar-content {
        background: linear-gradient(180deg, #f8f9fa 0%, #e9ecef 100%);
        padding: 1rem;
        border-radius: 10px;
    }
    @media (max-width: 768px) {
        .main-header {
            font-size: 2rem;
        }
        .section-header {
            font-size: 1.25rem;
        }
        .memory-card {
            padding: 1rem;
        }
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">🧠 EchoMind - Personal Memory Assistant</div>', unsafe_allow_html=True)

# Sidebar for information
with st.sidebar:
    st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
    st.header("ℹ️ About EchoMind")
    st.write("🧠 **EchoMind** is your personal memory assistant powered by AI embeddings.")
    st.write("**Key Features:**")
    st.write("✨ Add and store personal memories")
    st.write("🔍 Search for similar memories instantly")
    st.write("📚 Manage and organize your memories")
    st.markdown("---")
    st.write("**System Status:**")
    if check_api_status():
        st.success("🟢 API Connected")
    else:
        st.error("🔴 API Disconnected")
    st.markdown('</div>', unsafe_allow_html=True)

# Main content with tabs
tab1, tab2, tab3 = st.tabs(["📝 Add Memory", "🔍 Search Memories", "📚 Manage Memories"])

with tab1:
    render_add_memory()

with tab2:
    render_search_memories()

with tab3:
    render_manage_memories()

