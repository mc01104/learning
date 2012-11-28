#!/usr/bin/env python
'''
    This is a module that implements functions operating on graphs
'''

import numpy as np

#if needed, the list of colours can become longer or even of not fixed length
colors = ["red","green","blue","black"]


class GraphBundle(object):
	def __init__(self):
		object.__init__(self)
		self.labels = []
		self.edges = []
		self.adjacency_matrix = []
		self.adjacency_list = []
		self.property_str = ""
		if colors:
			self.edge_color = colors[0]
			colors.pop(0)
		else:
			self.edge_color = ""
	def update_state(self):
		self.adjacency_list = convert_adj_matrix_to_list(self.labels, self.adjacency_matrix)
		self.edges = create_edge_list(self.labels,self.adjacency_matrix)

class MultiPropGraphBundle(GraphBundle):
	def __init__(self):
		GraphBundle.__init__(self)
		self.graphs = []
		self.num_of_graphs = 0
		self.edge_color = ""
		self.edge_colormap = dict()
	def update_state(self):
		for graph in self.graphs:
			graph.update_state()
		self.flatten()
	def flatten(self):
		print len(self.graphs)
		if len(self.graphs) ==1:
			tmp_g = self.graphs[0]
		else:
			tmp_g = merge_graph(*self.graphs)
		self.labels = tmp_g.labels
		self.adjacency_matrix = tmp_g.adjacency_matrix
		GraphBundle.update_state(self)
	def get_subgraph(self,property_str):
		for graph in self.graphs:
			if graph.property_str == property_str:
				return graph
	def add_subgraph(self, *graph_objects):
		graph_object_list = list(graph_objects)
		graph_object = graph_object_list[0]
		graph_object_list.pop(0)		
		self.graphs.append(graph_object)
		self.update_state()
		self.update_colormap()
		if graph_object_list:
			return self.add_subgraph(*graph_object_list)
	def update_colormap(self):
		for edge in self.graphs[-1].edges:
			if self.edge_colormap.get(edge) == None:
				self.edge_colormap[edge] = self.graphs[-1].edge_color
			else:
				self.edge_colormap[edge] = "yellow"
	def update_edge_property_map(self):
		pass
		
#tested   
def convert_adj_matrix_to_list(node_list, adjacency_matrix):
	adj_list = dict()
	objects = []
	for i in range(len(adjacency_matrix)):
		mask = [item for item in range(len(adjacency_matrix[i])) if adjacency_matrix[i][item] == 1]
		objects = [node_list[k] for k in mask]
		if not objects:
			continue
		adj_list[node_list[i]] = objects
		
	return adj_list
			

#tested		
def convert_adj_list_to_matrix(node_list,adj_list):
	dim = len(node_list)
	adj_mtr = np.zeros((dim,dim) ,dtype = int)
	for key in adj_list.keys():
		i = node_list.index(key)
		for y in adj_list[key]:
			j = node_list.index(y)
			adj_mtr[i][j] = 1

	return adj_mtr		


def create_edge_list(node_list,adjacency_matrix):
	edges = []
	for(i,j) in get_indices(adjacency_matrix):
		edges.append((node_list[i],node_list[j]))
	return edges

			
#tested
def get_indices(matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if matrix[i][j] == 1:
				yield (i,j)


def is_directed(adjacency_matrix):
	if (adjacency_matrix.transpose() == adjacency_matrix).all():
		return 0
	return 1
						
#tested 
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
