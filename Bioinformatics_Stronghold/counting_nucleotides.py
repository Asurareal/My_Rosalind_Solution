def counting_nucleotides(filename):
  nucleotides = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
  for nucleotide, value in nucleotides.items():
      nucleotides[nucleotide] = filename.count(nucleotide)
  return nucleotides
if __name__ == '__main__':
    print(counting_nucleotides('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'))
