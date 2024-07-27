from Bio.Seq import Seq
DNA = Seq("AGCTAGCTAGAACTAGCTAGCTAGCAGCTAAAGCTAAA")
print(DNA)
print(DNA.complement())
print(DNA.reverse_complement())
