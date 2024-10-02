# Drawing a Phylogenetic Tree using PYTHON 
from Bio import Phylo
tree = Phylo.read("tree.dnd", "newick")        #parsing the file with putting two arguments : Tree.dnd,and newick format
print(Phylo.draw_ascii(tree))                  #print the tree into the ascii_art

import pylab

mrca = tree.common_ancestor({"name":"E"}, {"name":"F"})
mrca.color = "red"         #mrca= Most recent common ancestor

tree.rooted = True
Phylo.draw(tree)
