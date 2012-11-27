#! /usr/bin/env python

'''
	This is e first effort to perform learning on baysian networks using pebl and data from the net
'''
from pebl import data, result
from pebl.learner import *

#TODO: this should take as arguments
#      data  : txt file
#	   labels: node names and types of attributes
#	   conf  : configuration file - type of learnerm number of learners

if __name__ == "__main__":
		dataset = data.fromfile('/home/george/Desktop/diabetes_pebl_train.txt')
		dataset.discretize([0,1,2,3,4,5,6,7,8],[],5)
		#~ learner = greedy.GreedyLearner(dataset, max_iterations = 10000)
		#~ results = learner.run()
		#~ results.tohtml("results2")
		learners = [ greedy.GreedyLearner(dataset, max_iterations=1000000) for i in range(5) ] + \
		[ simanneal.SimulatedAnnealingLearner(dataset) for i in range(5) ]
		merged_result = result.merge([learner.run() for learner in learners])
		merged_result.tohtml("example3-result")
