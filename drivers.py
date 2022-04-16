'''
    DS 5010
    Spring 2022
    Project drivers

    Hongyan Yang
'''


def check_input(eg_list, lens_list):
    if len(eg_list) != len(lens_list):
        raise ValueError("Please input all edges' lengths.")
    else:
        ckd_egs, ckd_lens = [], []
        for i in range(len(eg_list)):
            temp_list = [each.upper() for each in eg_list[i]]
            sorted_eg = "".join(sorted(temp_list))
            if sorted_eg not in ckd_egs:
                ckd_egs.append(sorted_eg)
                ckd_lens.append(lens_list[i])
            elif ckd_lens[ckd_egs.index(sorted_eg)] == lens_list[i]:
                continue
            else:
                raise ValueError(f"Conflict lens input for edge {sorted_eg}.")
                print("2")
    return ckd_egs, ckd_lens

def check_cycle():
    pass

def generate_subsets(vertices_set):
    sets_dict, order = {}, len(vertices_set)
    vert_list = list(vertices_set)
    if order < 3:
        return None
    for i in range(2 ** order):
        to_bin = bin(i).replace("0b", "")
        bin_adj = (order - len(to_bin)) * "0" + to_bin
        subset = [vert_list[i] for i in range(order) if bin_adj[i] == "1"]
        key = sum([int(each) for each in bin_adj])
        if key in sets_dict:
            sets_dict[key].append(subset)
        else:
            sets_dict[key] = [subset]
    return sets_dict
        
        
    

    
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
        

        

