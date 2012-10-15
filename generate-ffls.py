# This script finds all 3-node motifs (FFLs) for a given input network
# Author: Bhanu Kishore Kampantula
# Date: 14th October 2012, 2:57 PM

# FFL a b c implies, a->b, a->c and b->c edges
# Input file should be an edgelist. 
# Creates an output file with a list of all FFLs

import networkx as nx
import sys, os

inFile = sys.argv[1] # Input file

fname = os.path.splitext(sys.argv[1])[0]
outFileFFLs = open(fname + '-FFLs.txt', "w") # Output file

G = nx.DiGraph()
ffl_counter = 0 # Counts number of FFLs
num_nodes = 0

for row in file(inFile):
	row = row.split()
	src = int(row[0])
	dest = int(row[1])
	G.add_edge(src, dest)

num_nodes = G.number_of_nodes()

for i in range(0,num_nodes):
	for j in range(0,num_nodes):
		for k in range(0,num_nodes):
			if G.has_edge(i, j) and G.has_edge(j,k) and G.has_edge(i,k):
				outFileFFLs.write(str(i) + ' ' + str(j) + ' ' + str(k) + '\n' )
				ffl_counter += 1
outFileFFLs.close()

print "Number of FFLs = ", ffl_counter
