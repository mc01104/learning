#!/usr/bin/env python
'''
    This is a module that implements a basic interface with knowrob in order to extract graphs for bayesian learning - testing autodoc
'''

import roslib;roslib.load_manifest('learning')
import json_prolog
from graph_util import GraphBundle
from graph_util import convert_adj_list_to_matrix
import numpy as np

#should I end the query when I am done???
#properties for class level implementation is missing!!!
		
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
	labels_with_uri = []
	for x in result_dict:
		if not x['S'] in labels_with_uri:
			labels_with_uri.append(x['S'])
		if not x['O'] in labels_with_uri:
			labels_with_uri.append(x['O'])	
	return labels_with_uri

#tested
#added code for the reflexive properties --- still a hack needs to be refactored
#reflexive hack is removed ---quality of code poor
def compute_adjacency_list(result_dict, prop_with_uri):
	adj_list = dict()
	refl = 0
	cmd = '''owl_has('%s',P,O)''' % prop_with_uri
	tmp_result = query(cmd)
	for ss in tmp_result:
		if ss['O'].split('#')[1] == "ReflexiveProperty":
			refl = 1

			
	for solution in result_dict:
		obj_list = []
		if adj_list.get(solution['S']) == None:
			if refl:
				obj_list.append(solution['S'])
		else:
			obj_list = adj_list.get(solution['S'])
		obj_list.append(solution['O'])
		adj_list[solution['S']] = obj_list
	

	if refl:
		obj_list = []	
		for solution in result_dict:
			if adj_list.get(solution['O']) == None:
				obj_list.append(solution['O'])
				adj_list[solution['O']] = obj_list
			
	return adj_list

#tested	
#stripped out the conversion from list to matrix in a separate function - tested    
def compute_adjacency_matrix(node_list,query_result, prop_with_uri):
	adj_list = compute_adjacency_list(query_result,prop_with_uri)
	adj_mtr = convert_adj_list_to_matrix(node_list,adj_list)
	return adj_mtr

    
#tested
def extract_graph(property_str,ontology_str = "test.owl"):
	ontology_uri = "http://www.hwu.ac.uk/osl/%s" % ontology_str
	prop_with_uri = ontology_uri + '#'  + property_str
	query_result = list(query_property(property_str,ontology_uri))
	result = GraphBundle()
	result.labels = get_labels(query_result)
	result.adjacency_matrix = compute_adjacency_matrix(result.labels,query_result, prop_with_uri)
	result.update_state()
	result.labels = [y.split('#')[1]	for y in result.labels]
	result.property_str = property_str
	return result


		
		
		
		
		
		
		
		
		
		
		
		
