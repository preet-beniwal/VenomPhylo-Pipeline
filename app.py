import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="VenomPhylo-Pipeline", layout="wide")

st.title("🐍 VenomPhylo-Pipeline")

# --- description ---
st.markdown("""
This is a Python pipeline I built to automate the phylogenetic analysis of snake venom proteins. 
It handles NCBI data fetching, MAFFT alignment, IQ-TREE generation, and mutation hotspot detection.
""")

st.sidebar.header("Pipeline Controls")
st.sidebar.write("Built for the UGC Snake Venom Project at GGDSD College.")
st.sidebar.write("Runs on standard laptops (i5/8GB RAM).")

results_dir = "results"

if not os.path.exists(results_dir):
    st.error("Results folder not found. Run the pipeline scripts first.")
else:
    st.success("Results loaded successfully.")
    
    # --- Section 1 ---
    st.header("1. Evolutionary Mutation Hotspots")
    st.write("Lower conservation scores mean the protein is mutating faster in that region.")
    
    csv_path = os.path.join(results_dir, "mutation_hotspots.csv")
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
        
        fig = px.bar(df, x="Position", y="Conservation_Score", 
                     color="Conservation_Score", color_continuous_scale="Viridis_r",
                     title="Amino Acid Conservation Across Alignment")
        st.plotly_chart(fig, use_container_width=True)
        
        st.subheader("Top 5 Most Variable Positions")
        top_5 = df.sort_values(by="Conservation_Score").head(5).reset_index(drop=True)
        top_5.index = top_5.index + 1
        st.dataframe(top_5)
    else:
        st.warning("Mutation hotspots data not found. Run analyze_evolution.py first.")

    # --- Section 2 ---
    st.header("2. Phylogenetic Tree")
    st.write("Maximum Likelihood tree generated with IQ-TREE (1000 Ultrafast Bootstraps).")
    
    tree_img_path = os.path.join(results_dir, "tree_visualization.png")
    if os.path.exists(tree_img_path):
        st.image(tree_img_path, caption="Maximum Likelihood Phylogenetic Tree", use_container_width=True)
        
        # --- Raw data ---

        tree_file_path = os.path.join(results_dir, "tree.treefile")
        if os.path.exists(tree_file_path):
            with open(tree_file_path, "r") as f:
                newick_string = f.read()
            with st.expander("View Raw Newick Tree Format"):
                st.text_area("Copy this into FigTree or iTOL", newick_string, height=150)
            st.info("You can download the `tree.treefile` and upload it to iTOL.com for a better looking tree.")
    else:
        st.warning("Tree image not found. Run `python analyze_evolution.py`.")