
def counting_nucleotides(dna_string):
    nucleotides = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for nucleotide in nucleotides.keys():
        nucleotides[nucleotide] = dna_string.count(nucleotide)
    return nucleotides

if __name__ == '__main__':
    seq = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
    results = counting_nucleotides(seq)
    print(f"{results['A']} {results['C']} {results['G']} {results['T']}")
