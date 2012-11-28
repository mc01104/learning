#! /usr/bin/env python

'''
	This is e first effort to perform learning on baysian networks using pebl and data from the net
'''
from pebl import data, result
from pebl.learner import *
from pebl_interface import graph2pebl
from pebl_interface import render_pebl_graph
import numpy as np

from time import gmtime, strftime

#TODO: this should take as arguments
#      data  : txt file
#	   labels: node names and types of attributes
#	   conf  : configuration file - type of learnerm number of learners

if __name__ == "__main__":
		dataset = data.fromfile('../datasets/diabetes/diabetes_pebl_train.txt')
		dataset.discretize(numbins=5)
		learner = greedy.GreedyLearner(dataset, max_iterations = 10000)
		#nodes_list = ["SAT","Difficulty","Intelligence","Grade","Letter"]
		#adjacency_matrix = np.array([[0,0,0,0,0],[0,0,0,1,0],[1,0,0,1,0],[0,0,0,0,1],[0,0,0,0,0]])
		#g = graph2pebl(nodes_list, adjacency_matrix)
		#learner.seed = g
		#render_pebl_graph(learner.seed,"initial")
		
		#~ learners = [ greedy.GreedyLearner(dataset, max_iterations=1000000) for i in range(5) ] + \
		#~ [ simanneal.SimulatedAnnealingLearner(dataset) for i in range(5) ]
		#~ merged_result = result.merge([learner.run() for learner in learners])
		
		results = learner.run()
		result_folder_str = "../experiments/diabetes_" + strftime("%Y-%m-%d_%H:%M:%S", gmtime())
		results.tohtml(result_folder_str)
		#~ merged_result.tohtml("result_folder_str")

