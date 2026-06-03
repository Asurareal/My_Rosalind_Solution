def counting_nucleotides(dna):
  nucleotides = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
  for nucleotide, value in nucleotides.items():
      nucleotides[nucleotide] = filename.count(dna)
  return nucleotides
if __name__ == '__main__':
    print(counting_nucleotides('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'))
