def file_txt(path):
  with open(path, 'r') as f:
    return f.read().strip()
    
if __name__ == "__main__":
    print(file_txt("/content/rosalind_rna.txt"))
