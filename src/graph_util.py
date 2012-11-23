#!/usr/bin/env python
'''
    This is a module that implements functions operating on graphs
'''

import numpy as np
from owl2graphAPI import *

#tested -- i will move this function to the MultiPropGraphClass as the flatten method
def merge_graph(graph_1, *graphs):
	nodes_list = []	
	args = list(graphs)

	if not args:
		raise Exception("you need at least two graphs to perform a merge operation")
	
	graph_2 = args[0]
	nodes_list.extend(graph_1.labels)
	nodes_list.extend([x for x in graph_2.labels if x not in graph_1.labels])
	
	dim = len(nodes_list) 
	adjacency_matrix = np.zeros((dim,dim) ,dtype = int)
	
	for (i,j) in get_indices(graph_1.adjacency_matrix):
		i_new = nodes_list.index(graph_1.labels[i])
		j_new = nodes_list.index(graph_1.labels[j])
		adjacency_matrix[i_new,j_new] = 1
		
	for (i,j) in get_indices(graph_2.adjacency_matrix):
		i_new = nodes_list.index(graph_2.labels[i])
		j_new = nodes_list.index(graph_2.labels[j])
		adjacency_matrix[i_new,j_new] = 1

	g = GraphBundle()
	g.labels = nodes_list
	g.adjacency_matrix = adjacency_matrix

	args.pop(0)
	
	if args:
		return merge_graph(g, *args)
		
	return g
