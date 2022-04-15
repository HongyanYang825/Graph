'''
    DS 5010
    Spring 2022
    Project drivers

    Hongyan Yang
'''


def to_vertices_set(edges_list):
    vertices = []
    for i in range(len(edges_list)):
        vertices.extend(list(edges_list[i]))
    vertices_set = set(vertices)
    return vertices_set

def connect_indices(edge, edges_list):
    indices = []
    for i in range(len(edges_list)):
        if not set(edge).isdisjoint(set(edges_list[i])):
           indices.append(i)
    return indices

def append_element(indices_list, from_list, to_list):
    for index in sorted(indices_list, reverse = True):
        to_append = from_list.pop(index)
        if to_append not in to_list:
            to_list.append(to_append)
    return to_list
        

        

