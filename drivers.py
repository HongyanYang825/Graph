'''
    DS 5010
    Spring 2022
    Project_Drivers_Applications_of_Graph_Theory_Topics

    Define a bunch of drivers to support the Graph class in
    graph.py

    Hongyan Yang
'''


from itertools import permutations

def check_input(eg_list, lens_list):
    '''
    Function -- check_input
    Check user inputs of edges and edge_lens for a Graph instance,
    transform inputs to correct format and raise errors when needed
    Parameters: eg_list (list)  -- a list of all edges in a graph
                lens_list (list) -- a list of ordered edge lengths      
    Return user inputs in correct format. Raise error and return None
    when inputs contains ValueError
    '''
    for each in lens_list:
        if each <= 0:
            raise ValueError("Please input positive edge_lengths.")
    if len(eg_list) != len(lens_list):
        # Raise error when not every input edge has been assigned
        # one and only one edge length
        raise ValueError("Please input all edges' lengths.")
    ckd_egs, ckd_lens = [], []
    for i in range(len(eg_list)):
        # Transform input edges to uppercases
        temp_list = [each.upper() for each in eg_list[i]]
        # Transform input edges to sorted order
        sorted_eg = "".join(sorted(temp_list))
        if sorted_eg not in ckd_egs:
            ckd_egs.append(sorted_eg)
            ckd_lens.append(lens_list[i])
        elif ckd_lens[ckd_egs.index(sorted_eg)] == lens_list[i]:
            # Remove duplicated input edge length of the same edge
            continue
        else:
            # Raise error when the same edge has been assigned
            # different edge lengths
            raise ValueError(f"Conflict lens input for edge {sorted_eg}.")
    return ckd_egs, ckd_lens

def to_vertices_set(edges_list):
    '''
    Function -- to_vertices_set
    Extract the vertices given all edges in a graph
    Parameters: edges_list (list) -- a list of all edges in a graph       
    Return a set of all vertices in a graph
    '''
    vertices = []
    for i in range(len(edges_list)):
        vertices.extend(list(edges_list[i]))
    vertices_set = set(vertices)    # Remove duplicated vertices
    return vertices_set

def connect_indices(edge, edges_list):
    '''
    Function -- connect_indices
    Find the indices of edges connected to a given edge in a graph
    Parameters: edge (str)  -- an edge in a graph
                edges_list (list) -- a list of edges    
    Return a list of indices of edges connected to a given edge
    '''
    indices = []
    for i in range(len(edges_list)):
        # Append the index if two edges are connected
        if not set(edge).isdisjoint(set(edges_list[i])):
           indices.append(i)
    return indices

def append_by_index(indices_list, from_list, to_list):
    '''
    Function -- append_by_index
    Append corresponding element to to_list given its index in from_list
    Parameters: indices_list (list)  -- a list of indices
                from_list (list) -- a list to get index from
                to_list (list) -- a list to append corresponding value into      
    Return a list with corresponding values appended 
    '''
    for index in sorted(indices_list, reverse = True):
        to_append = from_list.pop(index)
        # Only append unique values to the to_list
        if to_append not in to_list:
            to_list.append(to_append)
    return to_list
 
def append_by_values(value_list, from_list, to_list):
    '''
    Function -- append_by_values
    Append corresponding element to outputlist given its value in to_list 
    Parameters: value_list (list)  -- a list of values
                from_list (list) -- a list to get index from
                to_list (list) -- a list to get value from         
    Return a list with corresponding values appended
    '''
    output_list = []
    for value in value_list:
        index = from_list.index(value)
        output_list.append(to_list[index])
    return output_list

def generate_subsets(vertices_set):
    '''
    Function -- generate_subsets
    Grnerate all subsets, or the power set of a given set
    Parameters: vertices_set (set) -- a set contains all vertices of a given
                                      Graph instance        
    Returns a dictionary with keys as the sizes of the subsets and with value
    as a list of all subsets of the same size
    '''
    sets_dict, order = {}, len(vertices_set)
    vert_list = list(vertices_set)  # Convert set to list for ordered elements
    # Traverse all subsets in the power set
    for i in range(2 ** order):
        # Convert the index to a binary number and format it
        to_bin = bin(i).replace("0b", "")
        bin_adj = (order - len(to_bin)) * "0" + to_bin
        # Find the corresponding subset to the binary index number
        subset = [vert_list[i] for i in range(order) if bin_adj[i] == "1"]
        key = sum([int(each) for each in bin_adj])  # Key as the size of subset
        if key in sets_dict:
            sets_dict[key].append(subset)
        else:
            sets_dict[key] = [subset]
    return sets_dict

def sort_edge(cycle_set):
    '''
    Function -- sort_edge
    Sort edges' names in the cycle_set to ascending order
    Parameters: cycle_set (set) -- a set of edges in a cycle, edges' names are
                                   unformatted
    Return a formatted set of edges in a cycle
    '''
    sorted_set, eg_list = set(), list(cycle_set)
    # Format all edges' names in the cycle_set to ascending order
    for i in range(len(cycle_set)):
        temp_list = [each.upper() for each in eg_list[i]]
        sorted_eg = "".join(sorted(temp_list))
        # Add the edge with its name sorted to output set
        sorted_set.add(sorted_eg)
    return sorted_set

def generate_cycle(vertices_list):
    '''
    Function -- generate_cycle
    Generate a set of edges with formatted names given the input vertices
    Parameters: vertices_list (list)  -- A list of vertices from a subset of
                                         vertices of the vertices_set
    Return a set of edges in a cycle, edges are formatted
    '''
    cycle_set = set()
    # Generate a list of edges in arranged order
    for i in range(len(vertices_list)):
        if i != len(vertices_list) - 1:
            cycle_set.add(vertices_list[i] + vertices_list[i + 1])
        else:
            cycle_set.add(vertices_list[0] + vertices_list[i])
    # Format edges' names in the output set of edges
    cycle_set = sort_edge(cycle_set)
    return cycle_set

def reduce_duplicate_cycle(vertices_set):
    '''
    Function -- reduce_duplicate_cycle
    Remove duplicated cycles by the nature of cycle given a set of vertices 
    Parameters: vertices_set (set) -- a set contains all vertices of a given
                                      subset of the graph's vertices_set     
    Return a list of nonduplicated cycles given its vertices
    '''
    unique_cycles = []
    # Traverse all possible cycles given its vertices
    for each in list(permutations(vertices_set)):
        # Generate a set of edges with formatted names
        cycle_set = generate_cycle(each)
        if cycle_set not in unique_cycles:
            unique_cycles.append(cycle_set) # Append only unique set of edges
    return unique_cycles

def check_cycle(eg_list, vertices_set):
    '''
    Function -- check_cycle
    Check and return all existing cycles in the given graph
    Parameters: eg_list (list)  -- a list of all edges in a graph
                vertices_set (set) -- a set contains all vertices
                                      of a given Graph instance                             
    Returns a dictionary with keys as the sizes of the cycles and
    values as a list of all existing cycles with given size
    '''
    eg_set, cycle_dict = set(eg_list), {}
    # Generate a dictionary with keys as the sizes of the subsets and
    # values as a list of all subsets of the same size
    vertices_subsets = generate_subsets(vertices_set)
    # Return an empty dictionary if there's no potential cycles 
    if len(vertices_subsets) < 4:
        return {}
    # Only check subsets with more than 3 vertices inside
    potential_subsets = {key: vertices_subsets[key]
                         for key in range(3, len(vertices_subsets))}
    # Traverse all potential cycles in the given graph
    for key in potential_subsets.keys():
        for value in potential_subsets[key]:
            # Remove duplicated cycles by the nature of cycle
            unique_cycles = reduce_duplicate_cycle(value)
            for each in unique_cycles:
                # Check if the unique set of edges exists in the graph
                if each.issubset(eg_set):
                    if key in cycle_dict:
                        cycle_dict[key].append(each)
                    else:
                        cycle_dict[key] = [each]
    return cycle_dict

def cycle_is_exist(lens_list):
    '''
    Function -- cycle_is_exist
    Check if the edge lengths in the lens_list can form a cycle or not
    Parameters: lens_list (list)  -- a list of edge lengths in given cycle to
                                     be tested                             
    Return a Boolean indicates if the cycle can be created or not
    '''
    for each in lens_list:
        # A cycle can be formed iff any side's length is smaller than the sum
        # of other sides' lengths
        if each >= sum(lens_list) - each:
            return False
    return True
  
def test_cycles(cycles_dict, eg_list, lens_list):
    '''
    Function -- test_cycles
    Check if all cycles in a graph can be formed or not
    Parameters: cycles_dict (dict)  -- a dict of all cycles in the graph
                eg_list (list)  -- a list of all edges in a graph
                lens_list (list) -- a list of ordered edge lengths
    Raise ValueError if any cycle cannot be formed
    '''
    for key in cycles_dict:
        for value in cycles_dict[key]:
            cycle_lens = append_by_values(list(value), eg_list, lens_list)
            # Check if the cycle can be formed or not
            if not cycle_is_exist(cycle_lens):
                raise ValueError(f"Cycle {value} cannot be formed.")

def generate_path(path_tuple, sequence_tuple):
    '''
    Function -- generate_path
    Generate edges on a path given ordered vertices sequence
    Parameters: path_tuple (tuple)  -- a tuple consisting start and end
                                       vertices of the path
                sequence_tuple (tuple) -- a tuple consisting all vetices
                                          between start and end vertices       
    Return a list of all edges on the path and a set of these edges
    '''
    path_of_egs, sequence_list = [], list(sequence_tuple)
    # Sort the start and end vertices given the graph is undirected
    path_tuple = tuple(sorted(list(path_tuple)))
    # Insert start and end vertices to complete the path
    sequence_list.insert(0, path_tuple[0])
    sequence_list.append(path_tuple[-1])
    # Generate corresponding edges on the path
    for i in range(len(sequence_list) - 1):
        temp_list = sorted([sequence_list[i], sequence_list[i + 1]])
        path_of_egs.append("".join(temp_list))
    return path_of_egs, set(path_of_egs)

def path_len(path_list, eg_list, lens_list):
    '''
    Function -- path_len
    Calculate the path length given all edges on the path
    Parameters: path_list (list)  -- a list containing all edges on the path
                eg_list (list) -- a list of all edges in a graph
                lens_list (list) -- a list of ordered edge lengths
    Return a number representing the path length
    '''
    total_len = 0
    # Find edges corresponding lengths with index
    for each in path_list:
        total_len += lens_list[eg_list.index(each)]
    return total_len

def min_index(path_len_list):
    '''
    Function -- min_index
    Find the indices of minimum path length in the list and length value
    Parameters: path_len_list (list)  -- a list containing all possible paths'
                                         lengths       
    Return a list of the indices of minimum length, return length value
    '''
    min_len = min(path_len_list)
    # Traverse and find the indices of minimum path length
    min_indices = [index for index in range(len(path_len_list))
                   if path_len_list[index] == min_len]
    return min_indices, min_len

def print_path(path_list):
    '''
    Function -- print_path
    Output the shortest path in a vivid preset format
    Parameters: path_list (list)  -- a list of shortest paths' edges       
    Return a string presenting the shortest path in a vivid preset format
    '''
    path_route = ""
    for i in range(len(path_list) - 1):
        path_route += f"{path_list[i]} --> "
    path_route += path_list[-1]
    return path_route

def shortest_path(path_tuple, eg_list, lens_list):
    '''
    Function -- shortest_path
    Find and return the shortest path between two vertices in a given graph
    Parameters: path_tuple (tuple)  -- a tuple consisting start and end
                                       vertices of the path
                eg_list (list) -- a list of all edges in a graph
                lens_list (list) -- a list of ordered edge lengths 
    Return a list consisting all shortest paths, return the shortest length
    '''
    potential_paths, path_lens, shortest_paths = [], [], []
    # Convert the start and end vertices to correct format
    path_tuple = tuple([each.upper() for each in path_tuple])
    # Extract the vertices given all edges in a graph
    vertices_set = to_vertices_set(eg_list)
    if not set(path_tuple).issubset(vertices_set):
        # Raise ValueError if the start or end vertices not exist
        raise ValueError("Please input existing vertices.")
    else:
        seq_set = vertices_set - set(path_tuple)
        # Generate all potential vertices between the start and end vertices
        sub_seq_set = generate_subsets(seq_set)
        for key in sub_seq_set.keys():
            for value in sub_seq_set[key]:
                # Traverse all potential sequences on the path
                for each in list(permutations(value)):
                    # Generate all potential edges on the path
                    path = generate_path(path_tuple, each)
                    # Add path to potential shortest paths only if the edges
                    # on the path exist in the graph
                    if path[1].issubset(set(eg_list)):
                        potential_paths.append(path[0])
                        path_lens.append(path_len(path[0],eg_list, lens_list))
        # Find the indices of minimum path length and its value
        min_indices, min_len = min_index(path_lens)
        for each in min_indices:
            # Output the shortest path in a vivid preset format
            shortest_paths.append(print_path(potential_paths[each]))
        return shortest_paths, min_len

def height_of_tree(root, eg_list, vertices_set):
    lens_list, height_list = [1] * len(eg_list), []
    descendants = list(vertices_set - set(root))
    for each in descendants:
        height_list.append(shortest_path((root, each), eg_list, lens_list)[1])
    return max(height_list)
    
def optimal_root(eg_list, vertices_set):
    root_dict = {}
    for each in list(vertices_set):
        tree_height = height_of_tree(each, eg_list, vertices_set)
        if tree_height in root_dict:
            root_dict[tree_height].append(each)
        else:
            root_dict[tree_height] = [each]
    min_height = min(root_dict.keys())
    return root_dict[min_height], min_height

def tree_node_parent(node, root, eg_list):
    if node == root:
        return None
    lens_list = [1] * len(eg_list)
    path = shortest_path((node, root), eg_list, lens_list)[0][0]
    path_list = path.split(" --> ")
    for each in path_list:
        if node in set(each):
            parent = each.replace(node, "")
            return parent

def tree_node_children(node, root, eg_list):
    connected_nodes = set()
    parent = tree_node_parent(node, root, eg_list)
    if parent is None:
        parent = root
    for each in eg_list:
        if node in set(each):
            connected_nodes.update(set(each))
    children = connected_nodes - {node, parent}
    if len(children) == 0:
        return None
    return children

def tree_node_siblings(node, root, eg_list):
    parent = tree_node_parent(node, root, eg_list)
    if parent is None:
        return None
    children = tree_node_children(parent, root, eg_list)
    siblings = children - set(node)
    if len(siblings) == 0:
        return None
    return siblings

def parse_path_list(path_list):
    nodes_list = []
    for each in path_list:
        to_list = list(each)
        for each in to_list:
            if each not in nodes_list:
                nodes_list.append(each)
    return nodes_list
    
def tree_node_ancestors(node, root, eg_list):
    if node == root:
        return None
    lens_list = [1] * len(eg_list)
    path = shortest_path((node, root), eg_list, lens_list)[0][0]
    path_list = path.split(" --> ")
    ancestors = parse_path_list(path_list)
    ancestors.remove(node)
    if ancestors[0] == root:
        ancestors.reverse()
    return ancestors

def tree_node_descendents(node, root, eg_list):
    descendents, nodes_list = {}, list(to_vertices_set(eg_list))
    desc_list = [each for each in nodes_list if (each != root and node in
                 tree_node_ancestors(each, root, eg_list))]
    if len(desc_list) == 0:
        return None
    lens_list = [1] * len(eg_list)
    for each in desc_list:
        gen = shortest_path((each, node), eg_list, lens_list)[1]
        if gen in descendents:
            descendents[gen].append(each)
        else:
            descendents[gen] = [each]
    [each.sort() for each in descendents.values()]
    return descendents
    
def tree_node_neighbors(node, root, eg_list):
    depth_dict = tree_node_descendents(root, root, eg_list)
    for each in depth_dict.values():
        if node in each:
            return set(each) - set(node)

def parse_tree_depth(desc_dict):
    height = len(desc_dict) + 1
    width = max([len(each) for each in desc_dict.values()])
    return height, width
    
def rank_list(in_list):
    out_list, copy_in, sorted_in = [], in_list[:], sorted(in_list)
    for each in sorted_in:
        out_list.append(copy_in.index(each))
        copy_in[copy_in.index(each)] = None
    return out_list
