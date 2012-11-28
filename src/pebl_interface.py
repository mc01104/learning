#!/usr/bin/env python

'''
	This module implements an interface to the pebl library - bayesian learning in graphical models. 
'''

import pebl.network as pn
import pebl.data as pd
import numpy as np
import random

#tested
def graph2pebl(nodes_list, adjacency_matrix):
	nodes = []
	for n in nodes_list:
		nodes.append(pd.Variable(n))
		
	net = pn.Network(nodes)
	net.edges.adjacency_matrix = adjacency_matrix.astype('Bool')
	return net
	

#tested	
def render_pebl_graph(pebl_graph, filename_str):
	filename = filename_str + ".png"
	pebl_graph.as_image(filename)

#tested
def data_delimiter_change(filename_str,del_or,del_new):
	new_file_str = filename_str.split(".txt")[0] + "_pebl.txt"
	with open(filename_str) as infile:
		with open(new_file_str, 'w') as outfile:
			for line in infile:
				fields = line.split(del_or)
				outfile.write(del_new.join(fields))

#tested
def num_of_lines(fname):
	with open(fname) as f:
		for i, l in enumerate(f):
			pass
	return i + 1

#tested
#TODO: need to add name of nodes and type of data -- DONE -- #tested
#TODO: in the future I will add options for each label...
def generate_training_dataset(data_filename_str, header_filename_str):
	nlines = num_of_lines(data_filename_str)
	nlines_train = int(nlines/2)
	
	f = open(data_filename_str,'r')
	f_train = open(data_filename_str.split(".txt")[0] + "_train.txt",'w')
	f_test = open(data_filename_str.split(".txt")[0] + "_test.txt",'w')
	fh = open(header_filename_str,'r')

	headers =[item.split('\n')[0] for item in fh.readlines()]
	header_str = ""
	for x in headers:
		header_str += '''"%s"\t''' % x
	header_str += '\n'
	
	f_train.write(header_str)
	f_test.write(header_str)
	
	lines = f.readlines()

	if not len(headers) == len(lines[0].split('\t')):
		raise Exception("The number of labels doesn't correspond to the number of columns of the data file")
		
	random.shuffle(lines)

	for line in lines[0:nlines_train]:
		f_train.write(line)
		
	for line in lines[nlines_train+1:]:
		f_test.write(line)

	f_train.close()
	f_test.close()
	f.close()
