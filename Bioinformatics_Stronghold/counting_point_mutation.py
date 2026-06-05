
def counting_point_mutation(path):
    from Bioinformatics_Stronghold.utility import read_file
    dna_1, dna_2 = read_file(path).split("\n") # or .splitlines()
    count = 0
    for i , k in zip(dna_1, dna_2):
        if i != k:
            count += 1
    return count
if __name__ == "__main__":
    print(counting_point_mutation("/content/rosalind_hamm (1).txt"))
