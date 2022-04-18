'''
    DS 5010
    Spring 2022
    Project drivers

    Hongyan Yang
'''


from itertools import permutations

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
    return ckd_egs, ckd_lens

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

def sort_edge(cycle_set):
    sorted_set, eg_list = set(), list(cycle_set)
    for i in range(len(cycle_set)):
        temp_list = [each.upper() for each in eg_list[i]]
        sorted_eg = "".join(sorted(temp_list))
        sorted_set.add(sorted_eg)
    return sorted_set

def generate_cycle(vertices_list):
    cycle_set = set()
    for i in range(len(vertices_list)):
        if i != len(vertices_list) - 1:
            cycle_set.add(vertices_list[i] + vertices_list[i + 1])
        else:
            cycle_set.add(vertices_list[0] + vertices_list[i])
    cycle_set = sort_edge(cycle_set)
    return cycle_set

def reduce_duplicate_cycle(vertices_set):
    unique_cycles = []
    for each in list(permutations(vertices_set)):
        cycle_set = generate_cycle(each)
        if cycle_set not in unique_cycles:
            unique_cycles.append(cycle_set)
    return unique_cycles

def check_cycle(eg_list, vertices_set):
    eg_set, cycle_dict = set(eg_list), {}
    vertices_subsets = generate_subsets(vertices_set)
    if len(vertices_subsets) < 3:
        return None
    potential_subsets = {key: vertices_subsets[key]
                         for key in range(3, len(vertices_subsets))}
    for key in potential_subsets.keys():
        for value in potential_subsets[key]:
            unique_cycles = reduce_duplicate_cycle(value)
            for each in unique_cycles:
                if each.issubset(eg_set):
                    if key in cycle_dict:
                        cycle_dict[key].append(each)
                    else:
                        cycle_dict[key] = [each]
    return cycle_dict

def generate_path(path_tuple, sequence_tuple):
    path_of_egs, sequence_list = [], list(sequence_tuple)
    path_tuple = tuple(sorted(list(path_tuple)))
    sequence_list.insert(0, path_tuple[0])
    sequence_list.append(path_tuple[-1])
    for i in range(len(sequence_list) - 1):
        temp_list = sorted([sequence_list[i], sequence_list[i + 1]])
        path_of_egs.append("".join(temp_list))
    return path_of_egs, set(path_of_egs)

def print_path(path_list):
    path_route = ""
    for i in range(len(path_list) - 1):
        path_route += f"{path_list[i]} --> "
    path_route += path_list[-1]
    return path_route

def path_len(path_list, eg_list, lens_list):
    total_len = 0
    for each in path_list:
        total_len += lens_list[eg_list.index(each)]
    return total_len

def min_index(path_len_list):
    min_len = min(path_len_list)
    min_indices = [index for index in range(len(path_len_list))
                   if path_len_list[index] == min_len]
    return min_indices, min_len

def shortest_path(path_tuple, eg_list, lens_list):
    potential_paths, path_lens, shortest_paths = [], [], []
    path_tuple = tuple([each.upper() for each in path_tuple])
    vertices_set = to_vertices_set(eg_list)
    if not set(path_tuple).issubset(vertices_set):
        raise ValueError("Please input existing vertices.")
        return None
    else:
        seq_set = vertices_set - set(path_tuple)
        sub_seq_set = generate_subsets(seq_set)
        for key in sub_seq_set.keys():
            for value in sub_seq_set[key]:
                for each in list(permutations(value)):
                    path = generate_path(path_tuple, each)
                    if path[1].issubset(set(eg_list)):
                        potential_paths.append(path[0])
                        path_lens.append(path_len(path[0],eg_list, lens_list))
        min_indices, min_len = min_index(path_lens)
        for each in min_indices:
            shortest_paths.append(print_path(potential_paths[each]))
        return shortest_paths, min_len

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
        

        

