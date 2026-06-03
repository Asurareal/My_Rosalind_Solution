def reverse_complement(dna):
    dna = dna.upper()
    complement_table = str.maketrans("TCGA", "AGCT")
    complemented_dna = dna.translate(complement_table)
    return complemented_dna[::-1]
if __name__ == '__main__':
    print(reverse_complement("AAAACCCGGT"))
