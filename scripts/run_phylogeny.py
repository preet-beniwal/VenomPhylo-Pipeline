import subprocess
import os

#--- These path are specific to my laptop.If you move the folder, you have to change this Path.---

mafft_path = r"C:\mafft\mafft-win\mafft.bat"
iqtree_path = r"C:\iqtree\iqtree-2.4.0-Windows\bin\iqtree2.exe"

input_fasta = "../data/raw_sequences.fasta"
aligned_fasta = "../results/aligned.fasta"

print("Starting alignment with MAFFT...")

#--- Note: shell=True is needed to make the ">" redirect work ---

mafft_cmd = f'"{mafft_path}" --auto "{input_fasta}" > "{aligned_fasta}"'
subprocess.run(mafft_cmd, shell=True)

if os.path.exists(aligned_fasta):
    print(f"MAFFT Alignment complete. Saved to {aligned_fasta}\n")
else:
    print("MAFFT failed. Check your file paths.")
    exit()

#--- -bb 1000 for ultrafast bootstrap , -nt 2 so my laptop doesn't overheat, -pre is Prefix for all output files ---
iqtree_cmd = f'"{iqtree_path}" -s "{aligned_fasta}" -bb 1000 -nt 2 -pre "../results/tree"'
subprocess.run(iqtree_cmd, shell=True)

print("Pipeline finished.Check the result folder.")