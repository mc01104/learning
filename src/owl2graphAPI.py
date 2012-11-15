#!/usr/bin/env python
'''
    This is a module that implements a basic interface with knowrob in order to extract graphs for bayesian learning
'''

import roslib;roslib.load_manifest('learning')
import rospy
import json_prolog

class Graph_bundle:
    def __init__(self):
        labels = []
        adjacency_matrix = []
        
def query(query_str):
    prolog = json_prolog.Prolog()
    query = prolog.query(query_str)
    solution = query.solutions()
    query.finish()
    return solution

def query_property(property_str,namespace_str = "http://www.hwu.ac.uk/osl/test.owl"):
    property_with_namespace = "%s#%s" %(namespace_str,property_str)
    cmd = 'owl_has(S,%s,O)' % property_with_namespace
    result = query(cmd)
    return result

def get_labels(result_dict):
    labels = []
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
    