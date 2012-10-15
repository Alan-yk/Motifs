# This script finds all 3-node motifs (FFLs) for a given input network
# Author: Bhanu Kishore Kampantula
# Date: 14th October 2012, 2:57 PM

import networkx as nx
import sys, os, itertools
import numpy as np

inFile = sys.argv[1] # Input file

fname = os.path.splitext(sys.argv[1])[0]
outFileBifans = open(fname + '-Bifans.txt', "w") # Output file

G = nx.DiGraph()
bifan_counter = 0 # Counts number of Bifans
num_nodes = 0

for row in file(inFile):
	row = row.split()
	src = int(row[0])
	dest = int(row[1])
	G.add_edge(src, dest)

num_nodes = G.number_of_nodes()

for l in range(0,num_nodes):
	for m in range(0,num_nodes):
		for n in range(0,num_nodes):
			for o in range(0, num_nodes):
				if G.has_edge(l, n) and G.has_edge(l,o) and G.has_edge(m,n) and G.has_edge(m, o) and l != m and n != o:
					outFileBifans.write(str(l) + ' ' + str(m) + ' ' + str(n) + ' ' + str(o) + '\n' )
					bifan_counter += 1
outFileBifans.close()
print "Number of Bifans = ", bifan_counter/4

