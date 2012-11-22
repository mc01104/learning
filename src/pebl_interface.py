#!/bin/sh

'''
	This module implements an interface to the pebl library - bayesian learning in graphical models. 
'''

import pebl.network as pn
import pebl.data as pd
import numpy as np

def graph2pebl(nodes_list, adjacency_matrix):
	nodes = []
	for n in nodes_list:
		nodes.append(pd.Variable(n))
		
	net = pn.Network(nodes)
	net.edges.adjacency_matrix = adjacency_matrix.astype('Bool')
	return net
	
	
def render_pebl_graph(pebl_graph, filename_str):
	filename = filename_str + ".png"
	pebl_graph.as_image(filename)
