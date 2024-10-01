#parsing fasta file

from Bio import SeqIO
for sequence in SeqIO.parse('globin.fasta', "fasta"):
    print(sequence.id)
    print(repr(sequence.seq))
    print(len(sequence))
    
