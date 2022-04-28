'''
    DS 5010
    Spring 2022
    Project_Plot_Drivers_Applications_of_Graph_Theory_Topics

    Define a bunch of drivers to support the plot_tree() method of
    Graph class in graph.py

    Hongyan Yang
'''


import turtle

def draw_node(node_name, position):
    '''
    Function -- draw_node
    Create a turtle object to draw node with name at a given position
    Parameters: node_name (str) -- node's name
                position (tuple) -- a tuple of position on canvas     
    Return a turtle object representing the node
    '''
    end_position = (position[0], position[1] + 30)
    # Create a turtle to draw the node
    node = turtle.Turtle(visible = False)
    node.pen(pencolor = "#68aeba", pensize = 10)
    node.penup()
    node.goto(position) # Draw the node at given position
    node.pendown()
    node.circle(30, 360)
    node.pen(pencolor = "#f0d543")
    # Write node's name
    node.write(node_name, font = ("Arial",36, "bold"), align="center")
    node.penup()
    node.goto(end_position)
    return node

def draw_edge(edge_len, start_posi, end_posi):
    '''
    Function -- draw_edge
    Create a turtle object to draw edge with its length 
    Parameters: edge_len (int) -- edge's length
                start_posi (tuple) -- a tuple of the start position
                end_posi (tuple) -- a tuple of the end position
    Return a turtle object representing the edge
    '''
    mid_posi_x = (start_posi[0] - end_posi[0]) / 3 + end_posi[0]
    mid_posi_y = (start_posi[1] - end_posi[1]) / 3 + end_posi[1]
    mid_pos = (mid_posi_x, mid_posi_y)
    # Create a turtle to draw the edge
    edge = turtle.Turtle(visible = False)
    edge.pen(pencolor = "#C3C3C3", pensize = 4)
    edge.penup()
    edge.goto(start_posi)
    edge.pendown()
    edge.goto(end_posi) # Draw the edge from start_posi to end_posi
    edge.penup()
    edge.goto(mid_pos)
    edge.pendown()
    edge.pen(pencolor = "#7b7b78")
    # Write edge's length
    edge.write(edge_len, font = ("Arial",24, "normal"), align="center")
    return edge

def create_position(seq_dict, width = 800, height = 800):
    '''
    Function -- create_position
    Create a dictionary to record all nodes' positions on canvas
    Parameters: seq_dict (dict) -- a dict records all nodes at given depth
                width (int) -- canvas's width
                height (int) -- canvas's height
    Return a dictionary that records all nodes' positions
    '''
    posi_dict = {}
    for key in seq_dict.keys():
        coordinate = []
        for value in seq_dict[key]:
            # Layout all nodes seperate evenly at given depth
            coord_y = height / 2 - (height / (len(seq_dict) + 1)) * (key + 1)
            coord_x = - width / 2 + (width / (len(seq_dict[key]) + 1) *
                                     (seq_dict[key].index(value) + 1))
            coordinate.append((coord_x, coord_y))
        posi_dict[key] = coordinate
    return posi_dict
            
def draw_tree(seq_dict, link_dict, edges, edge_lens,
              width = 800, height = 800):
    '''
    Function -- draw_tree
    Draw a tree with all nodes and all existing edges 
    Parameters: seq_dict (dict) -- a dict records all nodes at given depth
                link_dict (dict) -- a dict records the parent of given node
                edges (list) -- a list of all edges in the tree
                edge_lens (list) -- a list of all edges' lens in the tree
                width (int) -- canvas's width
                height (int) -- canvas's height
    Draw the tree out on canvas
    '''
    turtle.TurtleScreen._RUNNING = True
    # Setup the canvas
    turtle.Screen().clear()
    turtle.Screen().setup(width = 800, height = 800)
    turtle.Screen().tracer(False)
    node_posi_dict, edges_dict = {}, {}
    # Create a dictionary to record all nodes' positions on canvas
    posi_dict = create_position(seq_dict, width = 800, height = 800)
    # Draw all nodes along with names
    for key in seq_dict.keys():
        for value in seq_dict[key]:
            node = draw_node(value, posi_dict[key][seq_dict[key].index(value)])
            node_posi_dict[value] = node
    # Draw all edges along with lengths
    for key in link_dict.keys():
        for i in range(len(link_dict[key])):
            linked_node = seq_dict[key][i]
            edge_name = "".join(sorted([link_dict[key][i], linked_node]))
            start_posi = node_posi_dict[link_dict[key][i]].position()
            end_posi = node_posi_dict[linked_node].position()
            edge_len = edge_lens[edges.index(edge_name)]
            edge = draw_edge(edge_len, start_posi, end_posi)
            edges_dict[edge_name] = edge
    for key in seq_dict.keys():
        for value in seq_dict[key]:
            node = draw_node(value, posi_dict[key][seq_dict[key].index(value)])
            node_posi_dict[value] = node
    turtle.Screen().tracer(True)
