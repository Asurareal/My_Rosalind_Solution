

def gc_calc(parsed_fasta_file): # should put the dictionary output from parse_fasta utility in it
    highest_percentage = -1.0 #as gc percent could never be negative
    highest_id = ""
    for header, sequence in parsed_fasta_file.items():
        gc_count = sequence.count('G') + sequence.count('C')
        percentage = (gc_count / len(sequence)) * 100
        print(f"ID: {header} | GC Content: {percentage:.6f}%")
        if percentage > highest_percentage:
            highest_percentage = percentage
            highest_id = header
    print(f"\nHIGHEST PERCENTAGE\n{highest_id}\n{highest_percentage:.6f}")
    return "copy only the highest percentage part for rosalind answer"
if __name__ == "__main__":
    import sys
    sys.path.append('/content/My_Rosalind_Solution/Bioinformatics_Stronghold')
    from utility import parse_fasta
    gc_calc(parse_fasta('/content/rosalind_gc.txt'))
