'''
    DS 5010
    Spring 2022
    Project_Applications_of_Graph_Theory_Topics

    Define and implement a Graph class to conduct graph operations
    based on the Graph Theory

    Hongyan Yang
'''


from drivers import *

class Graph:
    def __init__(self, edges, edge_lens, is_tree = False):
        '''
        Method -- __init__
        Create a new Graph instance by supplying edges and edge_lens
        for all edges in a graph with edge lenths set accordingly
        Parameters: edges (list) -- a list of all edges in a graph
                    edge_lens (list) -- a list of ordered edge lengths
                    is_tree (bool) -- a boolean indicates if it is a tree
        Create a new Graph instance and set a bunch of default attributes
        '''
        self.edges = edges
        self.edge_lens = edge_lens
        self.is_tree = is_tree
        # Set vertices attibute with get_vertices() method
        self.vertices = self.get_vertices()
        self.size = len(edges)
        self.order = len(self.vertices)
        # List all connected subgraphs as a dictionary
        # given the created Graph instance
        self.connected_subgraphs = self.connected_subgraphs()

    def set_vertices(self, vertices):
        '''
        Method -- set_vertices
        A set method to set graph's vertices manually
        Parameters: self -- input Graph instance
                    vertices (set) -- a set of graph vertices
        Set vertices value for a Graph instance
        '''
        self.vertices = vertices

    def get_vertices(self):
        '''
        Method -- get_vertices
        Extract vertices info given a graph's all edges
        Parameters: self -- input Graph instance
        Return a set of graph vertices
        '''
        vertices = []
        for i in range(len(self.edges)):
            vertices.extend(list(self.edges[i]))
        return set(vertices)

    def connected_subgraphs(self):
        '''
        Method -- connected_graphs
        Find all connected subgraphs in the given Graph instance and find
        their edge lenghs and vertices accordingly
        Parameters: self -- input Graph instance
        Return a dictionary with keys as the index of a certain sub_graph
        and values as its edges, edges' corresponding lengths and vertices
        '''
        dict, i = {}, 0
        eg_list, len_list = self.edges[:], self.edge_lens[:]
        while len(eg_list) != 0:
            dict[i] = ([eg_list[0]], [], set(eg_list[0]))
            indices = connect_indices(dict[i][2], eg_list)
            while len(indices) != 0:
                append_by_index(indices, eg_list, dict[i][0])
                dict[i][2].update(to_vertices_set(dict[i][0]))
                indices = connect_indices(dict[i][2], eg_list)
            sub_lens = append_by_values(dict[i][0], self.edges, self.edge_lens)
            dict[i][1].extend(sub_lens)
            i += 1
        return dict
