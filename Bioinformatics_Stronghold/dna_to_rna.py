def transcribe(dna):
  return dna.upper().replace("T", "U")
if __name__ == '__main__':
  print(transcribe("GATGGAACTTGACTACGTAAATT"))
