import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="PPI Analyzer", layout="wide")

# --- Initialize session state ---
if "active_page" not in st.session_state:
    st.session_state.active_page = "RegiPPI"

# --- CUSTOM CSS ---
st.markdown("""
    <style>
        section[data-testid="stSidebar"] {
            background-color: #1e1e2f;
            color: white;
        }

        .nav-link {
            display: block;
            width: 100%;
            text-align: left;
            padding: 0.75rem 1rem;
            margin: 0.25rem 0;
            background-color: #44446F;
            color: white;
            border: none;
            font-size: 16px;
            border-radius: 5px;
            transition: background-color 0.3s;
        }

        .nav-link:hover {
            background-color: #5858ad;
            cursor: pointer;
        }


    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.image("logo.png", use_container_width=True)

    nav_items = ["RegiPPI", "Embedding Explorer", "Model Inference","About"]

    for item in nav_items:
        is_active = "active" if st.session_state.active_page == item else ""
        st.markdown(
            f"""
            <form action="" method="get">
                <input type="hidden" name="page" value="{item}">
                <button class="nav-link {is_active}" type="submit">{item}</button>
            </form>
            """,
            unsafe_allow_html=True
        )

# --- Handle navigation based on query params ---
query_params = st.query_params
if "page" in query_params:
    selected_page = query_params["page"]
    st.session_state.active_page = selected_page

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
