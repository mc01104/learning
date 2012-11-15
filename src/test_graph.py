#!/usr/bin/env python
'''
    This is a just a test for the visualization functions i developed
'''

from plot_graph import render_graph
from plot_graph import create_graph
from owl2graphAPI import *
import numpy as np

a = np.array([[ 0,  0,  1],
              [ 0,  1,  0],
              [ 1,  0,  0]])

nodes = ["Creta","Lefkada","Cyprus"]
try:    
	test_graph = create_graph(nodes, a)
	render_graph(test_graph, "test_graph")
	labels = get_labels({})
	print labels
except Exception as inst:
	print inst.args[0]
