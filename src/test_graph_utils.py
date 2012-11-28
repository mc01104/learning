#!/usr/bin/env python

'''
    This is a just a test for the graph_util module
'''
from owl2graphAPI import *
from plot_graph import render_graph
from plot_graph import create_graph
from plot_graph import render_graph_color
from plot_graph import render_multi_prop_graph
from graph_util import *

from pebl_interface import data_delimiter_change
from pebl_interface import generate_training_dataset

import numpy as np
import rospy

rospy.init_node('test_owl2graphAPI')

a = ["george","mpampis","kwstas"]
b = ["george","eleni","kwstas","john"]
c = ["george","spyros","mpampis","kwstas"]

ad = np.array([[0,1,1],[0,1,1],[1,0,0]])
bd = np.array([[0,1,0,0],[1,1,1,1],[0,1,0,0],[0,0,0,0]])
cd = np.array([[0,1,1,0],[1,1,1,1],[0,1,0,0],[0,0,0,0]])

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

mg = MultiPropGraphBundle()
mg.add_subgraph(graph_a)
mg.add_subgraph(graph_b)
mg.add_subgraph(graph_c)


render_graph_color(mg,"test_merge_with multi")
#data_delimiter_change('../datasets/diabetes/diabetes.txt',',','\t')
render_multi_prop_graph(mg,"test_merge_with multi_color")
#generate_training_dataset('../datasets/diabetes/diabetes_pebl.txt','../datasets/diabetes/diabetes_names.txt')
