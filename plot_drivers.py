import turtle

from graph import *

name_dict = {2: ['B', 'D', 'G', 'H'], 1: ['C', 'F'], 3: ['E']}
seq_dict = {0: ['A'], 1: ['C', 'F'], 2: ['G', 'H', 'B', 'D'], 3: ['E']}
link_dict = {1: ['A', 'A'], 2: ['C', 'C', 'F', 'F'], 3: ['D']}
edges = ["AC", "CG", "CH", "AF", "BF", "DF", "DE"]
edge_lens = [1,2,3,4,5,6,7]

def draw_node(node_name, position):
    # Create a turtle to draw the node
    node = turtle.Turtle(visible = False)
    node.pen(pencolor = "#68aeba", pensize = 10)
    node.penup()
    node.goto(position)
    node.pendown()
    node.circle(30, 360)
    node.pen(pencolor = "#f0d543")
    node.write(node_name, font = ("Arial",36, "bold"), align="center")
    return node

def draw_edge(edge_len, start_posi, end_posi):
    mid_posi_x = (start_posi[0] + end_posi[0]) / 2
    mid_posi_y = (start_posi[1] + end_posi[1]) / 2
    mid_pos = (mid_posi_x, mid_posi_y)
    edge = turtle.Turtle(visible = False)
    edge.pen(pencolor = "#7b7b78", pensize = 4)
    edge.penup()
    edge.goto(start_posi)
    edge.pendown()
    edge.goto(end_posi)
    edge.penup()
    edge.goto(mid_pos)
    edge.pendown()
    edge.pen(pencolor = "#7b7b78")
    edge.write(edge_len, font = ("Arial",24, "normal"), align="center")
    return edge

def create_position(seq_dict, width = 800, height = 800):
    posi_dict = {}
    for key in seq_dict.keys():
        coordinate = []
        for value in seq_dict[key]:
            coord_y = height / 2 - (height / (len(seq_dict) + 1)) * (key + 1)
            coord_x = - width / 2 + (width / (len(seq_dict[key]) + 1) *
                                     (seq_dict[key].index(value) + 1))
            coordinate.append((coord_x, coord_y))
        posi_dict[key] = coordinate
    return posi_dict
            
def draw_tree(seq_dict, link_dict, edges, edge_lens,
              width = 800, height = 800):
    turtle.TurtleScreen._RUNNING = True
    turtle.Screen().setup(width = 800, height = 800)
    turtle.Screen().tracer(False)
    node_posi_dict, edges_dict = {}, {}
    posi_dict = create_position(seq_dict, width = 800, height = 800)
    for key in seq_dict.keys():
        for value in seq_dict[key]:
            node = draw_node(value, posi_dict[key][seq_dict[key].index(value)])
            node_posi_dict[value] = node
    for key in link_dict.keys():
        for i in range(len(link_dict[key])):
            linked_node = seq_dict[key][i]
            edge_name = "".join(sorted([link_dict[key][i], linked_node]))
            start_posi = node_posi_dict[link_dict[key][i]].position()
            end_posi = node_posi_dict[linked_node].position()
            edge_len = edge_lens[edges.index(edge_name)]
            edge = draw_edge(edge_len, start_posi, end_posi)
            edges_dict[edge_name] = edge
    turtle.Screen().tracer(True)
    turtle.done()
    return node_posi_dict, edges_dict


