import streamlit as st
from PIL import Image

def run():
    st.header("📘 About REGi-PPI")
    
    st.markdown("""
    **REGi-PPI** (Regression Based Edge Prediction of Protein-Protein Interaction) is a deep learning model designed to predict PPI edges using Graph Neural Networks.  
    It is built to determine potential interactions of unknown proteins within a PPI network and assign interaction scores.
    """)

    st.markdown("---")
    st.subheader("📊 System Diagram & Methodology")

    col1, col2 = st.columns([1.2, 1])
    with col1:
        st.markdown("""
        REGi-PPI works by predicting edges between proteins using embeddings and GNN-based regression:
        
        - **Data Source**: STRING database (interactions filtered with score ≥ 400)
        - **Embedding**: Protein sequences are encoded using **ProtBERT**
        - **Graph Construction**:
            - Nodes: Protein embeddings
            - Edges: Combined embeddings + STRING score
        - **GNN Models**: Trained using **GCN** and **GAT**
        - **Output**: Interaction probability & combined score of new protein
        
        The model enables edge-level prediction and regression — predicting both presence and interaction strength.
        """)
    with col2:
        image = Image.open("about_app/model_image.png")  # Your workflow/architecture image
        st.image(image, caption="Figure: REGi-PPI Workflow", use_container_width=True)

    st.markdown("---")
    st.subheader("🚀 Novelty of REGi-PPI")
    st.markdown("""
    While models like **Struct2Graph** handle edge classification, REGi-PPI introduces regression to learn edge weights and return quantified scores of protein interaction.  
    The method is lightweight, simple, and flexible—allowing rapid predictions using pre-trained embeddings and GNNs.
    """)

    st.markdown("---")
    st.subheader("🌍 Societal & Environmental Impact")
    st.markdown("""
    - **Healthcare**: Enables faster diagnosis and treatment discovery via PPI mapping  
    - **Sustainability**: Reduces lab waste and power usage through computational prediction  
    - **Ethics**: Bypasses unnecessary experiments, encouraging data-driven safe research  
    """)

    st.markdown("---")
    st.subheader("💼 Business Model & Future Scope")
    st.markdown("""
    The model serves as a **prototype** for scalable microbiological deep learning applications.  
    Future goals include:
    - Setting up a research center focused on GNNs in bioinformatics
    - Scaling models using **high-performance compute clusters**
    - Partnering with institutions that manage sensitive biological data  
    Inspired by tools like **AlphaFold-3**, REGi-PPI could shape the next era of AI-based microbiological discovery.
    """)

    st.markdown("---")
    st.subheader("🧪 Results")
    col1, col2, col3 = st.columns(3)
    col1.image("about_app/result1.png", caption="Result 1", use_container_width=True)
    col2.image("about_app/result2.png", caption="Result 2", use_container_width=True)
    col3.image("about_app/result3.png", caption="Result 3", use_container_width=True)

    st.markdown("---")
    st.subheader("📌 Conclusion")
    st.markdown("""
    REGi-PPI was trained as a **CPU-based prototype** with simplified subgraph sampling.  
    Planned upgrades:
    - Extend to multiple **benchmark datasets**
    - Experiment with **advanced sampling strategies**
    - Build a **custom GNN architecture**
    - Package the app using **Docker** and **Hydra** for portability across devices
    """)

    st.markdown("---")
    st.markdown("""
    <div style="text-align: center;">
        <strong>© 2025 REGi-PPI Team</strong><br>
    </div>
    """, unsafe_allow_html=True)
