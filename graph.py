'''
    DS 5010
    Spring 2022
    Project_Applications_of_Graph_Theory_Topics

    Define and implement a Graph class to conduct graph operations
    based on the Graph Theory

    Define and implement a Tree subclass to conduct tree operations
    and plot the given tree object

    Hongyan Yang
'''


from drivers import *
from plot_drivers import *

class Graph:
    def __init__(self, edges, edge_lens):
        '''
        Method -- __init__
        Create a new Graph instance by supplying edges and edge_lens
        for all edges in a graph with edge lenths set accordingly
        Parameters: edges (list) -- a list of all edges in a graph
                    edge_lens (list) -- a list of ordered edge lengths
        Create a new Graph instance and set a bunch of default attributes
        '''
        ckd_egs, ckd_lens = check_input(edges, edge_lens)
        self.edges, self.edge_lens = ckd_egs, ckd_lens
        test_cycles(self.get_cycles(), self.edges, self.edge_lens)
        # Set vertices attibute with set_vertices() method
        self.vertices = self.set_vertices()
        self.size = len(self.edges)
        self.order = len(self.vertices)
        # List all connected subgraphs as a dictionary
        # given the created Graph instance
        self.connected_subgraphs = self.set_subgraphs()
        # an undirected graph is tree iff there is no cycle in the graph  
        # and the graph is connected.
        if len(self.connected_subgraphs) == 1 and len(self.get_cycles()) == 0:
            self.is_a_tree = True
        else:
            self.is_a_tree = False

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
        self.edges, self.edge_lens = ckd_egs, ckd_lens
        test_cycles(self.get_cycles(), self.edges, self.edge_lens)
        if (len(self.get_connected_subgraphs()) == 1 and
            len(self.get_cycles()) == 0):
            self.is_a_tree = True
        else:
            self.is_a_tree = False

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

    def is_tree(self):
        '''
        Method -- is_tree
        Check if the graph is a tree or not
        Parameters: self -- input Graph instance
        Return is_a_tree attribute of a Graph instance
        '''
        return self.is_a_tree

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

    def get_cycles(self):
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

class Tree(Graph):
    def __init__(self, edges, edge_lens, root):
        '''
        Method -- __init__
        Create a new Tree instance by supplying edges, edge_lens and root
        Parameters: edges (list) -- a list of all edges in a tree
                    edge_lens (list) -- a list of ordered edge lengths
                    root (str) -- tree's root, which can be changed later
        Create a new Graph instance and set a bunch of default attributes
        '''
        self.root = root
        # the Tree subclass inherits _init_ method from the Graph class
        super().__init__(edges, edge_lens)
        self.name_dict = self.get_descendents(self.root)
        self.seq_dict = self.name_to_seq(self.name_dict)
        self.link_dict = self.name_to_link(self.seq_dict, root)
        self.seq_dict[0] = [self.root]

    def set_root(self, root):
        '''
        Method -- set_root
        A set method to set tree's root
        Parameters: self -- input Tree instance
                    root (str) -- tree's root
        Set root attribute for a Tree instance
        '''
        self.root = root
        self.name_dict = self.get_descendents(self.root)
        self.seq_dict = self.name_to_seq(self.name_dict)
        self.link_dict = self.name_to_link(self.seq_dict, root)
        self.seq_dict[0] = [self.root]

    def get_root(self):
        '''
        Method -- get_root
        A get method to get tree's root
        Parameters: self -- input Tree instance
        Return the root attribute of a Tree instance
        '''
        return self.root

    def roots_with_min_height(self):
        '''
        Method -- roots_with_min_height
        Find and return all roots that create the tree with min height
        Parameters: self -- input Tree instance
        Return a set of roots provide min height
        '''
        self.vertices = self.set_vertices()
        return optimal_root(self.edges, self.vertices)

    def get_parent(self, node):
        '''
        Method -- get_parent
        Find and return the parent of one node in the tree
        Parameters: self -- input Tree instance
                    node (str) -- the node to find the parent of
        Return the parent of a given node
        '''
        return tree_node_parent(node, self.root, self.edges)

    def get_children(self, node):
        '''
        Method -- get_children
        Find and return all the children of one node in the tree
        Parameters: self -- input Tree instance
                    node (str) -- the node to find the children of
        Return all the children of a given node
        '''
        return tree_node_children(node, self.root, self.edges)

    def get_siblings(self, node):
        '''
        Method -- get_siblings
        Find and return all the siblings of one node in the tree
        Parameters: self -- input Tree instance
                    node (str) -- the node to find the siblings of
        Return all the siblings of a given node
        '''
        return tree_node_siblings(node, self.root, self.edges)
    
    def get_ancestors(self, node):
        '''
        Method -- get_ancestors
        Find and return all the ancestors of one node in the tree
        Parameters: self -- input Tree instance
                    node (str) -- the node to find the ancestors of
        Return all the ancestors of a given node from leaves to root as a list
        '''
        return tree_node_ancestors(node, self.root, self.edges)

    def get_descendents(self, node):
        '''
        Method -- get_descendents
        Find and return all the descendents of one node in the tree
        Parameters: self -- input Tree instance
                    node (str) -- the node to find the descendents of
        Return all the descendents as a dictionary with key as the genenration
        and values as a set of same generation descendents
        '''
        return tree_node_descendents(node, self.root, self.edges)

    def get_neighbors(self, node):
        '''
        Method -- get_neighbors
        Find and return all the neighbors of one node in the tree
        Parameters: self -- input Tree instance
                    node (str) -- the node to find the neighbors of
        Return all the neighbors of a given node as a set
        '''
        return tree_node_neighbors(node, self.root, self.edges)

    def name_to_seq(self, name_dict):
        '''
        Method -- name_to_seq
        Find the sequence of all nodes at a given depth of the tree
        Parameters: self -- input Tree instance
                    name_dict (dict) -- a dict of all nodes at a given depth
        Return a dict records the sequence of nodes at every depth
        '''
        seq_dict = {1: list(range(len(name_dict[1])))}
        if len(name_dict) == 1:
            return seq_dict
        for key in range(2, len(name_dict) + 1):
            temp_list = []
            for value in name_dict[key]:
                parent = self.get_parent(value)
                i = seq_dict[key-1][name_dict[key -1].index(parent)]
                temp_list.append(i)
            seq_dict[key] = rank_list(temp_list)
        for key in seq_dict:
                seq_dict[key] = [name_dict[key][each]
                                 for each in seq_dict[key]]
        return seq_dict

    def name_to_link(self, seq_dict, root):
        '''
        Method -- name_to_link
        Find the sequence of all nodes' parents at a given depth of the tree
        Parameters: self -- input Tree instance
                    seq_dict (dict) -- a dict records the sequence
                    root (str) -- tree's root
        Return a dict records nodes' parents at every depth
        '''
        link_dict = {1:[]}
        for key in seq_dict:
            for value in seq_dict[key]:
                if key == 1:
                    link_dict[key].append(root)
                else:
                    parent = self.get_parent(value)
                    i = seq_dict[key -1].index(parent)
                    if key in link_dict:
                        link_dict[key].append(i)
                    else:
                        link_dict[key] = [i]
        for key in link_dict:
            if key == 1:
                pass
            else:
                link_dict[key] = [seq_dict[key - 1][each]
                                 for each in link_dict[key]]
        return link_dict
    
    def plot_tree(self):
        '''
        Method -- plot_tree
        Plot the given tree
        Parameters: self -- input Tree instance
        Plot the tree given the current root
        '''
        return draw_tree(self.seq_dict, self.link_dict, self.edges,
                         self.edge_lens, width = 800, height = 800)
