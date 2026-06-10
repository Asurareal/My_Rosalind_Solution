def read_file(path):
    with open(path, 'r') as f:
        return f.read().strip()

def parse_fasta(path):
    with open(path, 'r') as f:
        raw_file = f.read().strip()
    sequences = {}
    chunks = raw_file.split(">")[1:]
    for chunk in chunks:
        lines = chunk.splitlines()       
        header = lines[0]                
        dna_sequence = "".join(lines[1:]) 
        sequences[header] = dna_sequence 
    return sequences
if __name__ == "__main__":
    print(parse_fasta("/content/FASTA.txt"))
    print(read_file("/content/file.txt"))
