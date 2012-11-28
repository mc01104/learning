#!/usr/bin/env python
# This program adds up integers in the command line


'''
    This is a visualization library for the graphs that are extracted from knowrob. It gets as input
    an adjacency matrix and renders and saves the graph in the current folder
'''

# Import graphviz
import sys
sys.path.append('..')
sys.path.append('/usr/lib/graphviz/python/')
sys.path.append('/usr/lib/pyshared/python2.7')
import gv
import numpy as np


# Import pygraph
from pygraph.classes.graph import graph
from pygraph.classes.digraph import digraph
from pygraph.readwrite.dot import write

from graph_util import is_directed

def render_graph(graph_obj, filename_str):
	dot = write(graph_obj)
	gvv = gv.readstring(dot)
	gv.layout(gvv,'dot')
	filename = "%s.png" % filename_str
	gv.render(gvv,'png',filename)


def create_graph(nodes_list, adjacency_matrix, label_str = ""):

	if not (adjacency_matrix.shape[0] == adjacency_matrix.shape[1]):
		raise Exception("adjacency matrix should be square")
	
	if not (len(nodes_list) == adjacency_matrix.shape[0]):
		raise Exception("number of nodes is inconsistent with the number of available node labels")
	
	if is_directed(adjacency_matrix):
		gr = digraph()
	else:
		gr = graph()
		adjacency_matrix = np.triu(adjacency_matrix)
		
	gr.add_nodes(nodes_list)

	for x in range(len(adjacency_matrix)): 
		for y in range(len(adjacency_matrix[x])): 
			if adjacency_matrix[x][y] == 1:
				gr.add_edge((nodes_list[x],nodes_list[y]),label = label_str)
				
	return gr

# This is an alternative implementation that will support more formatting for the visualization

def render_graph_color(graph_object,filename_str):
	import pydot

	node_list, adjacency_matrix = graph_object.labels, graph_object.adjacency_matrix

	if not (adjacency_matrix.shape[0] == adjacency_matrix.shape[1]):
		raise Exception("adjacency matrix should be square")
	
	if not (len(nodes_list) == adjacency_matrix.shape[0]):
		raise Exception("number of nodes is inconsistent with the number of available node labels")
			 
	if is_directed(adjacency_matrix):
		graph = pydot.Dot(graph_type='digraph')
	else:
		graph = pydot.Dot(graph_type='graph')
		
	nodes_dot=[]

	for n in node_list:
		tmp = pydot.Node(n)
		nodes_dot.append(tmp)
		graph.add_node(tmp)

	for i in range(len(adjacency_matrix)):
		for j in range(len(adjacency_matrix[i])):
			if adjacency_matrix[i][j] == 1:
				graph.add_edge(pydot.Edge(nodes_dot[i], nodes_dot[j], label=graph_object.property_str, labelfontcolor="#009933", fontsize="10.0", color=graph_object.edge_color))
	
	name =  "%s.png" % filename_str
	graph.write_png(name)
	
