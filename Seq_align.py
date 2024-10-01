# Sequence Alignment 
from Bio import Align

aligner = Align.PairwiseAligner(match_score = 1.0)

seq1 = "GACTAG"         #This gives the default global alignment, also, it gives optimal alignment through the sequence.
seq2 = "GACTAT"

score = aligner.score(seq1, seq2)   

print(f"The score of the alignment is {score}")

alignments = aligner.align(seq1, seq2)

for alignment in alignments:
    print(alignment)

aligner.mode = "local"     #  We have to choose local for loacl alignment. 

seq3 = "AGATCTAT"
seq4 = "GATCAT"
scorelocal = aligner.score(seq3, seq4)

print(f"The local alignment score is {scorelocal}")

alignlocal = aligner.align(seq3, seq4)
for x in alignlocal:
    print(x) 


#Here, it give the result 6 because 6 is matching the sequence.