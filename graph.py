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
        ckd_egs, ckd_lens = check_input(edges, edge_lens)
        self.edges = ckd_egs
        self.edge_lens = ckd_lens
        self.is_tree = is_tree
        # Set vertices attibute with set_vertices() method
        self.vertices = self.set_vertices()
        self.size = len(self.edges)
        self.order = len(self.vertices)
        # List all connected subgraphs as a dictionary
        # given the created Graph instance
        self.connected_subgraphs = self.set_subgraphs()

    def set_edges_and_lens(self, edges, edge_lens):
        '''
        Method -- set_edges_and_lens
        A method to check and set graph's edges and their corresponding
        edge lengths
        Parameters: self -- input Graph instance
                    edges (list) -- a list of all edges in a graph
                    edge_lens (list) -- a list of ordered edge lengths
        Check and set edges and edge_lens attribute for a Graph instance
        '''
        ckd_egs, ckd_lens = check_input(edges, edge_lens)
        self.edges = ckd_egs
        self.edge_lens = ckd_lens

    def set_vertices(self):
        '''
        Method -- set_vertices
        Extract vertices info given a graph's all edges
        Parameters: self -- input Graph instance
        Return a set of graph vertices
        '''
        vertices = []
        # Add all nodes of existing edges to the list
        for i in range(len(self.edges)):
            vertices.extend(list(self.edges[i]))
        # Return a set of vertices to remove duplicates
        return set(vertices)

    def set_subgraphs(self):
        '''
        Method -- set_subgraphs
        Find all connected subgraphs in the given Graph instance and find
        their edge lenghs and vertices accordingly
        Parameters: self -- input Graph instance
        Return a dictionary with keys as the index of a certain sub_graph
        and values as its edges, edges' corresponding lengths and vertices
        '''
        dict, i = {}, 0
        eg_list, len_list = self.edges[:], self.edge_lens[:]
        # Keep searching new subgraphs while there're edges remaining
        while len(eg_list) != 0:
            # Create a new item in dict for each subgraph
            dict[i] = ([eg_list[0]], [], set(eg_list[0]))
            # Get the indices of edges connecting to the subgraph
            indices = connect_indices(dict[i][2], eg_list)
            # Keep adding edges to the subgraph until all edges are compared
            while len(indices) != 0:
                # Append conncted edges to the subgraph
                append_by_index(indices, eg_list, dict[i][0])
                # Update the subgraph's vertices set
                dict[i][2].update(to_vertices_set(dict[i][0]))
                indices = connect_indices(dict[i][2], eg_list)
            # Form a list of corresponding edge lengths to the subgraph
            # Extend the list to subgraphs dictionary
            sub_lens = append_by_values(dict[i][0], self.edges, self.edge_lens)
            dict[i][1].extend(sub_lens)
            i += 1
        return dict

    def get_edges(self):
        '''
        Method -- get_edges
        A get method to get graph's edges
        Parameters: self -- input Graph instance
        Return edges attribute of a Graph instance
        '''
        return self.edges

    def get_edge_lens(self):
        '''
        Method -- get_edge_lens
        A get method to get graph's edge_lens
        Parameters: self -- input Graph instance
        Return edge_lens attribute of a Graph instance
        '''
        return self.edge_lens

    def get_vertices(self):
        '''
        Method -- get_vertices
        A get method to get graph's vertices
        Parameters: self -- input Graph instance
        Return vertices attribute of a Graph instance
        '''
        self.vertices = self.set_vertices()
        return self.vertices

    def get_size(self):
        '''
        Method -- get_size
        A get method to get graph's size
        Parameters: self -- input Graph instance
        Return size attribute of a Graph instance
        '''
        self.size = len(self.edges)
        return self.size

    def get_order(self):
        '''
        Method -- get_order
        A get method to get graph's order
        Parameters: self -- input Graph instance
        Return order attribute of a Graph instance
        '''
        self.vertices = self.set_vertices()
        self.order = len(self.vertices)
        return self.order

    def get_connected_subgraphs(self):
        '''
        Method -- get_connected_subgraphs
        A get method to get graph's all connected_subgraphs
        Parameters: self -- input Graph instance
        Return connected_subgraphs attribute of a Graph instance
        '''
        self.connected_subgraphs = self.set_subgraphs()
        return self.connected_subgraphs

    def cycles(self):
        '''
        Method -- cycles
        A method to get graph's all cycles
        Parameters: self -- input Graph instance
        Return a dictionary with keys as the sizes of the cycles and
        values as a list of all existing cycles with given size
        '''
        self.vertices = self.set_vertices()
        return check_cycle(self.edges, self.vertices)

    def get_shortest_path(self, path_tuple):
        '''
        Method -- get_shortest_path
        A method to get graph's all shortest paths between two vertices
        Parameters: self -- input Graph instance
                    path_tuple (tuple)  -- a tuple consisting start and end
                                           vertices of the path
        Return a list consisting all shortest paths, return the shortest length
        '''
        return shortest_path(path_tuple, self.edges, self.edge_lens)
