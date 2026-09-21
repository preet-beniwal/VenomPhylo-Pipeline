from Bio import AlignIO
from collections import Counter
import pandas as pd

# --- Path to aligned sequences ---
aligned_fasta = "../results/aligned.fasta"
output_csv = "../results/mutation_hotspots.csv"

print("Starting VenomPhylo-Pipeline")

# --- Loading alignment ---
try:
    alignment = AlignIO.read(aligned_fasta, "fasta")
    print(f"Loaded alignment with {len(alignment)} sequences.")
except Exception as e:
    print(f"Error loading alignment: {e}")
    exit()

# --- Calculating conservation per position ---
data = []
for i in range(alignment.get_alignment_length()):
    column = alignment[:, i]
    # Remove gaps (represented by '-')
    clean_column = [aa for aa in column if aa != '-']
    
    if len(clean_column) > 0:
        counts = Counter(clean_column)
        most_common_aa, most_common_count = counts.most_common(1)[0]
        conservation_score = (most_common_count / len(clean_column)) * 100
        
        data.append({
            "Position": i + 1,
            "Most_Common_AA": most_common_aa,
            "Conservation_Score": round(conservation_score, 2),
            "Variation_Count": len(counts)
        })

# --- Saving to CSV ---
df = pd.DataFrame(data)
df.to_csv(output_csv, index=False)

print(f"Analysis complete! Saved to {output_csv}")
print(f"Total positions analyzed: {len(df)}")
print("\nTop 5 Most Variable Positions (Mutation Hotspots):")
print(df.sort_values(by="Conservation_Score").head(5).to_string(index=False))

# --- Rendering PHYLOGENETIC TREE ---

import matplotlib.pyplot as plt
from Bio import Phylo

tree_file = "../results/tree.treefile"
image_output = "../results/tree_visualization.png"

print("\nRendering phylogenetic tree image...")
try:
    tree = Phylo.read(tree_file, "newick")
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(1, 1, 1)
    Phylo.draw(tree, axes=ax, do_show=False)
    plt.title("Phylogenetic Tree of Snake Venom Proteins")
    plt.savefig(image_output, dpi=300, bbox_inches='tight')
    print(f"Tree image saved to {image_output}")
except Exception as e:
    print(f"Error rendering tree: {e}")