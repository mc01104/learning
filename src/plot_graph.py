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

from graph_util import is_directed, get_indices

#became obsolete - consider removing
def render_graph(graph_obj, filename_str):
	dot = write(graph_obj)
	gvv = gv.readstring(dot)
	gv.layout(gvv,'dot')
	filename = "%s.png" % filename_str
	gv.render(gvv,'png',filename)

#beacame obsolete - consider removing
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

	for (x,y) in get_indices(adjacency_matrix):
		gr.add_edge((nodes_list[x],nodes_list[y]),label = label_str)
		
	return gr

# This is an alternative implementation that will support more formatting for the visualization

def render_graph_color(graph_object,filename_str):
	import pydot

	node_list, adjacency_matrix = graph_object.labels, graph_object.adjacency_matrix

	if not (adjacency_matrix.shape[0] == adjacency_matrix.shape[1]):
		raise Exception("adjacency matrix should be square")
	
	if not (len(node_list) == adjacency_matrix.shape[0]):
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

	for (i,j) in get_indices(adjacency_matrix):
				graph.add_edge(pydot.Edge(nodes_dot[i], nodes_dot[j], label=graph_object.property_str, labelfontcolor="#009933", fontsize="10.0", color=graph_object.edge_color))
	
	name =  "%s.png" % filename_str
	graph.write_png(name)

#TODO: merge this function with the above
#TODO: implement mixed graph, the two opposing arrows don't look nice!
#TODO: if this module ends-up being one function -> move it to graph_util	
#TODO: also display multiple properties on edges.
def render_multi_prop_graph(multi_prop_graph,filename_str):
		
	import pydot

	node_list, adjacency_matrix = multi_prop_graph.labels, multi_prop_graph.adjacency_matrix

	if not (adjacency_matrix.shape[0] == adjacency_matrix.shape[1]):
		raise Exception("adjacency matrix should be square")
	
	if not (len(node_list) == adjacency_matrix.shape[0]):
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

	for (i,j) in get_indices(adjacency_matrix):
				graph.add_edge(pydot.Edge(nodes_dot[i], nodes_dot[j], label=multi_prop_graph.property_str, labelfontcolor="#009933", fontsize="10.0", color=multi_prop_graph.edge_colormap[node_list[i],node_list[j]]))
	
	name =  "%s.png" % filename_str
	graph.write_png(name)
			
		
		
		
		
		
		
