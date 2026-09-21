from Bio import Entrez, SeqIO

# --- providing email to NCBI to prevents from getting blocked.---
Entrez.email = "preetbeniwal1309@gmail.com"

# --- Before i tried PLA2 only which gave me zero results then i gave two protein name options and got 20 Results.---
query = "Echis carinatus[Organism] AND (PLA2 OR Phospholipase)"
print(f"Searching NCBI for: {query}...")

# --- I've put the limit to 100 as I'm working on 8GB RAM Windows, so that my laptop doesn't runout of RAM or the program crash. ---
handle = Entrez.esearch(db="protein", term=query, retmax=100)
record = Entrez.read(handle)
handle.close()

id_list = record["IdList"]
print(f"Found {len(id_list)} sequences.")

# --- Fetching the sequences in FASTA format ---
if len(id_list) > 0:
    print("Downloading sequences...")
    fetch_handle = Entrez.efetch(db="protein", id=id_list, rettype="fasta", retmode="text")
    
    #---Saving the sequences to data folder ---
    output_file = "../data/raw_sequences.fasta"
    with open(output_file, "w") as f:
        f.write(fetch_handle.read())
    
    fetch_handle.close()
    print(f"Success! Sequences saved to {output_file}")
else:
    print("No sequences found. Try a different query.")