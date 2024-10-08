DNA = '''ATCGATCGATGGACCAAATTCGCCCGCGTGCGTGCGTAGCCGGGCTGCCGGCCGGATAGCGATCCAAGCTA
GCGCGCGCCGGCGCGCCCAGCCGCGCGCGAAATTAGTCGGCCCAAAAAGGTGATGCTTAGCTAGCTACGATGCTAGGCTA
GCTAGTCCAAGCTAAAGCTAGCTGATCGGTTTCCAGCTCAGCTAGCAAACCAAAAAAAAAACCAATTAAAAAGGTCCAAAT'''

#gc_count = (total_gc / total_length) * 100

g_count = DNA.count("G")
c_count = DNA.count("C")

total_gc = DNA.count("G") + DNA.count("C")
total_length = len(DNA)

gc_percentage = (total_gc / total_length) * 100

print(gc_percentage)
print(f"The total gc_percentage of this DNA sequence is {round(gc_percentage, 2)}%")




