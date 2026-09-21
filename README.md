# 🐍 VenomPhylo-Pipeline

An automated Python framework for comparative molecular evolution and variant mapping of Indian snake venom toxins. 

## 🚀 Features
*   **Automated Data Engine:** Fetches protein sequences directly from NCBI via Biopython.
*   **CLI Execution Wrapper:** Automates MAFFT alignment and IQ-TREE Maximum Likelihood tree generation.
*   **Evolutionary Calculator:** Calculates amino acid conservation scores to identify rapid mutation hotspots.
*   **Interactive Dashboard:** Built with Streamlit for real-time visualization of evolutionary data.

## ⚙️ Installation
This pipeline is designed to run on standard consumer laptops (Tested on Windows, Intel i5, 8GB RAM).
1. Clone this repository: `git clone https://github.com/yourusername/VenomPhylo-Pipeline.git`
2. Create the conda environment: `conda env create -f environment.yml`
3. Activate the environment: `conda activate venom_project`

## 🛠️ Prerequisites (Windows)
This pipeline uses command-line bioinformatics tools. On Windows, download and extract the following to `C:\`:
*   [MAFFT for Windows](https://mafft.cbrc.jp/alignment/software/windows.html) (Extract to `C:\mafft`)
*   [IQ-TREE 2](https://github.com/iqtree/iqtree2/releases) (Extract to `C:\iqtree`)

## 🏃 Usage
Run the pipeline in order:
1. `python scripts/fetch_data.py` (Downloads sequences)
2. `python scripts/run_phylogeny.py` (Aligns and builds tree)
3. `python scripts/analyze_evolution.py` (Calculates mutation hotspots)
4. `streamlit run app.py` (Launches dashboard)

## 📊 Outputs
*   `results/aligned.fasta`: Multiple sequence alignment
*   `results/tree.treefile`: Newick phylogeny tree
*   `results/mutation_hotspots.csv`: Conservation scores per amino acid position