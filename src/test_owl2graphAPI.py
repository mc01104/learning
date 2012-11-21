#!/usr/bin/env python
'''
    This is a just a test for the owl2graphAPI
'''

from owl2graphAPI import *
from plot_graph import render_graph
from plot_graph import create_graph
from plot_graph import render_graph_color

import numpy as np
import rospy

rospy.init_node('test_owl2graphAPI')

#query for objects that are connected with specific properties
solutions = list(query_property("eats"))

#get the labels for the graph
labels = get_labels(solutions)
print "---- labels -----" 
print labels

#compute the adjacency_list
adj_list = compute_adjacency_list(solutions,"http://www.hwu.ac.uk/osl/test.owl#eats")
print "---- adjacency_list ----"
print adj_list

#compute the adjacency matrix
adj_mtr = compute_adjacency_matrix(labels,solutions,"http://www.hwu.ac.uk/osl/test.owl#eats")
print "---- adjacency_matrix ----"
print adj_mtr

#testing the final (actual client function)
g = Graph_bundle()
g = extract_graph("eats")
print "---- Graph Bundle ----"
print "Graph_bundle:Labels ="
print g.labels
print "Graph_bundle: Adjacency Matrix ="
print g.adjacency_matrix

#save the graph as an image
g_plot = create_graph(g.labels,g.adjacency_matrix,"eats")
render_graph(g_plot, "g_graph")

render_graph_color(g.labels,g.adjacency_matrix,"g_graph_color")
