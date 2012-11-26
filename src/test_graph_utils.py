#!/usr/bin/env python

from owl2graphAPI import *
from plot_graph import render_graph
from plot_graph import create_graph
from plot_graph import render_graph_color
from graph_util import merge_graph


import numpy as np
import rospy

rospy.init_node('test_owl2graphAPI')

a = ["george","mpampis","kwstas"]
b = ["george","eleni","kwstas","john"]
c = ["george","spyros","mpampis","kwstas"]

ad = np.array([[0,1,1],[0,1,1],[1,0,0]])
bd = np.array([[0,1,0,0],[1,1,1,1],[0,1,0,0],[0,0,0,0]])
cd = np.array([[0,1,0,0],[1,1,1,1],[0,1,0,0],[0,0,0,0]])

graph_a = GraphBundle()
graph_b = GraphBundle()
graph_c = GraphBundle()

graph_a.labels = a
graph_a.adjacency_matrix = ad
graph_b.labels = b
graph_b.adjacency_matrix = bd
graph_c.labels = c
graph_c.adjacency_matrix = cd

graph_a.update_state()
graph_a.update_state()
graph_c.update_state()

graph_a.property_str = "isFriend"
graph_b.property_str = "hasSexWith"

g = merge_graph(graph_a,graph_b, graph_c)
render_graph_color(g,"test_merge")
