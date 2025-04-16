import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="PPI Analyzer", layout="wide")

# --- Session state for active page ---
if "active_page" not in st.session_state:
    st.session_state.active_page = "RegiPPI"

# --- CUSTOM CSS ---
st.markdown("""
    <style>
        section[data-testid="stSidebar"] {
            background-color: #1e1e2f;
            color: white;
        }

        .nav-container {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        .stButton>button {
            width: 100%;
            text-align: left;
            padding: 0.75rem 1rem;
            border-radius: 8px;
            background-color: #44446F;
            color: white;
            border: none;
            font-size: 16px;
            transition: background-color 0.3s;
        }

        .stButton>button:hover {
            background-color: #5858ad;
        }

        .stButton>button.active {
            background-color: #7070db !important;
        }

    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.image("logo.png", use_container_width=True)
    st.markdown('<div class="nav-container">', unsafe_allow_html=True)

    nav_items = ["RegiPPI", "Embedding Explorer", "Model Inference", "About"]

    for item in nav_items:
        # Render button and track if clicked
        if st.button(item, key=f"nav_{item}"):
            st.session_state.active_page = item

        # Inject custom class for active one
        st.markdown(f"""
            <script>
                const btn = window.parent.document.querySelectorAll('button[kind="secondary"][data-testid="stButton"]');
                const labels = {nav_items};
                const active = "{st.session_state.active_page}";
                btn.forEach((b, i) => {{
                    if (b.innerText.trim() === active) {{
                        b.classList.add("active");
                    }}
                }});
            </script>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# --- MAIN CONTENT ---
st.title("Protein-Protein Interaction Analysis Platform")

if st.session_state.active_page == "RegiPPI":
    st.header("🔬 RegiPPI")
    st.write("RegiPPI Section Content...")

elif st.session_state.active_page == "Embedding Explorer":
    st.header("🧬 Embedding Explorer")
    st.write("Embedding Explorer Content...")

elif st.session_state.active_page == "Model Inference":
    st.header("🧠 Siamese Network Inference")
    st.write("Model Inference Content...")

elif st.session_state.active_page == "About":
    st.header("📘 About")
    st.write("This app analyzes protein-protein interactions using various tools.")
