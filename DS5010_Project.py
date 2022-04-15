'''
    DS 5010
    Spring 2022
    Project

    Hongyan Yang
'''


from drivers import *

class Graph:
    def __init__(self, edges, edge_lens, is_tree = None):
        self.edges = edges
        self.edge_lens = edge_lens
        self.size = len(edges)
        self.order = len(self.get_vertices())

    def set_vertices(self, vertices):
        self.vertices = vertices

    def get_vertices(self):
        vertices = []
        for i in range(len(self.edges)):
            vertices.extend(list(self.edges[i]))
        self.vertices = set(vertices)
        return self.vertices

    def is_connected(self):
        dict, i = {}, 0
        eg_list, len_list = self.edges[:], self.edge_lens[:]
        while len(eg_list) != 0:
            dict[i] = ([eg_list[0]], [len_list[0]], set(eg_list[0]))
            indices = connect_indices(dict[i][2], eg_list)
            while len(indices) != 0:
                append_element(indices, eg_list, dict[i][0])
                append_element(indices, len_list, dict[i][1])
                dict[i][2].update(to_vertices_set(dict[i][0]))
                indices = connect_indices(dict[i][2], eg_list)
            i += 1
        return dict
        



        
        
        
        

        

