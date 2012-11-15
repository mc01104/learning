#!/usr/bin/env python
'''
    This is a module that implements a basic interface with knowrob in order to extract graphs for bayesian learning
'''

import roslib;roslib.load_manifest('learning')
import rospy
import json_prolog

#should I end the query when I am done???

class Graph_bundle:
    def __init__(self):
        labels = []
        adjacency_matrix = []

#tested        
def query(query_str):
    prolog = json_prolog.Prolog()
    query = prolog.query(query_str)
    solution = query.solutions()
    return solution

#tested
def query_property(property_str,namespace_str = "http://www.hwu.ac.uk/osl/test.owl"):
    property_with_namespace = "%s#%s" %(namespace_str,property_str)
    cmd = '''owl_has(S,'%s',O)''' % property_with_namespace
    result = query(cmd)
    return result

#tested
def get_labels(result_dict):
	labels = []
	labels_with_uri = []
	for x in result_dict:
		if not x['S'] in labels_with_uri:
			labels_with_uri.append(x['S'])
		if not x['O'] in labels_with_uri:
			labels_with_uri.append(x['O'])

	labels = [y.split('#')[1]	for y in labels_with_uri]
	return labels
    
def compute_adjacency_matrix(node_list,query_result):
    rs=[]
    return rs
    
def verify_graph(labels_list, adjacency_mtr):
    return 1
    
def extract_graph(property_str,ontology_str = "test.owl"):
    ontology_uri = "http://www.hwu.ac.uk/osl/%s" % ontology_str
    query_result = query_property(property_str,ontology_uri)
    result = Graph_bundle()
    result.labels = get_labels(query_result)
    result.adjacency_matrix = compute_adjacency_matrix(result.labels,query_result)
    return result
    
