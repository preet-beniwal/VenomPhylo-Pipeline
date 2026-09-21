# 🐍 VenomPhylo-Pipeline

An automated Python framework for the phylogenetic analysis of Indian snake venom proteins. 

I built this tool to solve a specific bottleneck in the UGC-funded snake venom project at our Bioinformatics department. Previously, analyzing venom evolution required manually searching NCBI, downloading sequences one by one, and clicking through desktop GUIs like MEGA. This pipeline automates the entire process—from fetching raw data to generating a visual dashboard.

##  Why I Built This
Most bioinformatics tools are designed for Linux clusters or high-end servers. I wanted to create a reproducible pipeline that runs on a standard lab laptop (**Intel i5, 8GB RAM**) without crashing, so any student in the department can run it without needing specialized hardware or software setup skills.

##  Pipeline Features
1. **Data Scraping:** Automatically queries NCBI via Biopython and downloads venom toxin sequences.
2. **Alignment & Phylogeny:** Wraps MAFFT and IQ-TREE in a Python CLI wrapper to generate Maximum Likelihood trees.
3. **Evolutionary Analysis:** Calculates amino acid conservation scores to identify mutation hotspots (a lightweight alternative to running PAML on Windows).
4. **Interactive Dashboard:** A Streamlit web app that visualizes the tree, charts mutation hotspots, and displays raw Newick data for downstream tools like iTOL.

##  Prerequisites & Installation (Windows)

Because some of these tools are natively built for Linux, getting them to run on Windows requires a few specific steps:

**1. Set up the Python Environment**
```bash
git clone https://github.com/preet-benival/VenomPhylo-Pipeline.git
cd VenomPhylo-Pipeline
conda env create -f environment.yml
conda activate venom_project

**2. Install the Command-Line Tools (Manually)**
Conda often fails to install these specific bio-tools on Windows, so I had to download the binaries manually. Make sure they are extracted to the root of your C: drive:

· MAFFT for Windows (Extract to C:\mafft)
· IQ-TREE 2 (Extract to C:\iqtree)

 Usage

Run the scripts in order. I recommend keeping the Streamlit app in a separate terminal window.

```bash
# 1. Fetch sequences from NCBI (Tested with Naja naja PLA2)
python scripts/fetch_data.py

# 2. Align sequences and build the phylogenetic tree
python scripts/run_phylogeny.py

# 3. Calculate mutation hotspots and render the tree image
python scripts/analyze_evolution.py

# 4. Launch the interactive dashboard
streamlit run app.py
```

 Outputs

After running the pipeline, check the results/ folder for:

· aligned.fasta: Multiple sequence alignment
· tree.treefile: Newick phylogeny tree (can be uploaded to iTOL)
· tree_visualization.png: Rendered phylogenetic tree image
· mutation_hotspots.csv: Conservation scores per amino acid position

🔬 Future Work & Scaling

Right now, this pipeline serves as a proof-of-concept on a single species. The next step is to expand the data engine to automatically loop through the "Big Four" medically significant Indian venomous snakes (Naja naja, Bungarus caeruleus, Daboia russelii, Echis carinatus) to perform comparative venom evolution analysis.

👤 Author

Preet Beniwal
BCA Student | Department of Computer Science, GGDSD College, Chandigarh
Built for the UGC Snake Venom Evolution Project (PI: Prof. Varinder Kumar)

```

---

### 🚀 How to Commit and Push This Update to GitHub

Once you have saved the file locally on your laptop, go back to your **Anaconda Prompt** and run these commands one by one:

1. Make sure you are in your main project folder:
   ```bash
   cd C:\Users\Preet\OneDrive\Documents\VenomPhylo-Pipeline
```

1. Add the updated file:
   ```bash
   git add README.md
   ```
2. Commit the change:
   ```bash
   git commit -m "docs: update README with detailed context, prerequisites, and future scaling plans"
   ```
3. Push it to GitHub:
   ```bash
   git push origin main
   ```