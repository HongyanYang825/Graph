'''
    DS 5010
    Spring 2022
    Unit_Tests_for_Project_Applications_of_Graph_Theory_Topics

    Define and implement a Graph_Test class to test functionality
    of Graph class and its subclass Tree class

    * Note: The .plot_tree() method which plots the tree graph
    cannot be tested with unnittest class. So it should be tested
    seperately with the following inputs:

    edges = ["AC", "CG", "CH", "AF", "BF", "DF", "DE"]
    edge_lens = [1,2,3,4,5,6,7]
    # Create a Tree object with root "A"
    tree = Tree(edges, edge_lens, "A")
    tree.plot_tree()    # Test the .plot_tree() method
    tree.set_root("F")    # Change root to node "F"
    tree.plot_tree()    # Test the .plot_tree() with new root
    tree.set_root("C")    # Change root to node "C"
    tree.plot_tree()    # Test the .plot_tree() with root "C"

    Naseem Alfaqeh, Hongyan Yang
'''


import unittest
from graph import *
 
class Graph_Test(unittest.TestCase):
    def test_bad_init_1(self):
        # Test bad input: edges and lens not one on one
        with self.assertRaises(ValueError):
            edges = ['AB', 'AC', 'BC']
            edge_lens = [2, 2, 3, 2]
            graph = Graph(edges, edge_lens)

    def test_bad_init_2(self):
        # Test bad input: conflict lens input for edge AC
        with self.assertRaises(ValueError):
            edges = ['AB', 'AC', 'BC', 'AC']
            edge_lens = [2, 2, 3, 1]
            graph = Graph(edges, edge_lens) 

    def test_bad_init_3(self):
        # Test bad input: Triangle ABC cannot be formed with
        # given edge lengths
        with self.assertRaises(ValueError):
            edges = ['AB', 'AC', 'BC']
            edge_lens = [1, 1, 3]
            graph = Graph(edges, edge_lens)
            
    def test_get_edges(self):
        # Test the .get_edges() method
        edges = ['Ab', 'ca', 'Cb', 'AC']
        edge_lens = [2, 2, 3, 2]
        graph = Graph(edges, edge_lens)
        self.assertEqual(graph.get_edges(), ['AB', 'AC', 'BC'])
    
    def test_get_edge_lens(self):
        # Test the .get_edge_lens() method
        edges = ['Ab', 'ca', 'Cb', 'AC']
        edge_lens = [2, 2, 3, 2]
        graph = Graph(edges, edge_lens)
        self.assertEqual(graph.get_edge_lens(), [2, 2, 3])

    def test_get_vertices(self):
        # Test the .get_vertices() method
        edges = ['Ab', 'ca', 'Cb', 'AC']
        edge_lens = [2, 2, 3, 2]
        graph = Graph(edges, edge_lens)
        self.assertEqual(graph.get_vertices(), {"A", "B", "C"})
        
    def test_get_size(self):
        # Test the .get_size() method
        edges = ['Ab', 'ca', 'Cb', 'AC']
        edge_lens = [2, 2, 3, 2]
        graph = Graph(edges, edge_lens)
        self.assertEqual(graph.get_size(), 3)
        
    def test_get_order(self):
        # Test the .get_order() method
        edges = ['Ab', 'ca', 'Cb', 'AC']
        edge_lens = [2, 2, 3, 2]
        graph = Graph(edges, edge_lens)
        self.assertEqual(graph.get_order(), 3)

    def test_get_connected_subgraphs(self):
        edges= ['AB', 'AC', 'BC', 'DE', 'EF', 'FG', 'DG']
        edge_lens= [2, 2, 2, 1, 1, 1, 1]
        graph = Graph(edges, edge_lens)
        # Should return two connected sub_graphs in the graph
        self.assertEqual(graph.get_connected_subgraphs(),
                         {0: (['AB', 'BC', 'AC'], [2, 2, 2],
                              {'A', 'B', 'C'}),
                          1: (['DE', 'DG', 'EF', 'FG'], [1, 1, 1, 1],
                              {'D', 'E', 'F', 'G'})})
        
    def test_get_cycles(self):
        edges = ['AB', 'AD', 'BC', 'CD', 'BE', 'CE']
        edge_lens = [2, 2, 2, 2, 3, 3]
        graph = Graph(edges, edge_lens)
        self.assertEqual(graph.get_cycles(),
                         {3: [{'BE', 'CE', 'BC'}],
                          4: [{'AB', 'CD', 'BC', 'AD'}],
                          5: [{'AB', 'CD', 'AD', 'BE', 'CE'}]})
        
    def test_get_shortest_path(self):
        edges = ['AC', 'AD', 'BC', 'BD', 'BE', 'CE', 'EF', 'BF', 'AG']
        edge_lens = [2, 2, 2, 2, 1, 2, 1, 1, 1]
        graph = Graph(edges, edge_lens)
        path_tuple = ("D", "E")
        self.assertEqual(graph.get_shortest_path(path_tuple),
                         (['BD --> BE'], 3))
   
    def test_is_tree(self):
       edges = ["AC", "CG", "CH", "AF", "BF", "DF", "DE"]
       edge_lens = [1,2,3,4,5,6,7]
       graph = Graph(edges, edge_lens)
       self.assertEqual(graph.is_tree(), True)

    def test_get_root(self):
       edges = ["AC", "CG", "CH", "AF", "BF", "DF", "DE"]
       edge_lens = [1,2,3,4,5,6,7]
       tree = Tree(edges, edge_lens, "A")
       self.assertEqual(tree.get_root(), 'A')
       
    def test_get_parent(self):
       edges = ["AC", "CG", "CH", "AF", "BF", "DF", "DE"]
       edge_lens = [1,2,3,4,5,6,7]
       tree = Tree(edges, edge_lens, "A")
       self.assertEqual(tree.get_parent("G"), 'C')   

    def test_get_children(self):
       edges = ["AC", "CG", "CH", "AF", "BF", "DF", "DE"]
       edge_lens = [1,2,3,4,5,6,7]
       tree = Tree(edges, edge_lens, "A")
       self.assertEqual(tree.get_children("F"), {'B', 'D'})  
       
    def test_get_siblings(self):
       edges = ["AC", "CG", "CH", "AF", "BF", "DF", "DE"]
       edge_lens = [1,2,3,4,5,6,7]
       tree = Tree(edges, edge_lens, "A")
       self.assertEqual(tree.get_siblings("G"), {'H'})  
       
    def test_get_same_level_nodes(self):
       edges = ["AC", "CG", "CH", "AF", "BF", "DF", "DE"]
       edge_lens = [1,2,3,4,5,6,7]
       tree = Tree(edges, edge_lens, "A")
       self.assertEqual(tree.get_same_level_nodes("G"), {'H', 'B', 'D'})  
       
    def test_get_ancestors(self):
       edges = ["AC", "CG", "CH", "AF", "BF", "DF", "DE"]
       edge_lens = [1,2,3,4,5,6,7]
       tree = Tree(edges, edge_lens, "A")
       self.assertEqual(tree.get_ancestors("E"), ['D', 'F', 'A']) 
       
    def test_get_descendents(self):
       edges = ["AC", "CG", "CH", "AF", "BF", "DF", "DE"]
       edge_lens = [1,2,3,4,5,6,7]
       tree = Tree(edges, edge_lens, "A")
       self.assertEqual(tree.get_descendents("A"),
                        {3: ['E'], 1: ['C', 'F'],
                         2: ['B', 'D', 'G', 'H']}) 

    def test_roots_with_min_height(self):
       edges = ["AC", "CG", "CH", "AF", "BF", "DF", "DE"]
       edge_lens = [1,2,3,4,5,6,7]
       tree = Tree(edges, edge_lens, "A")
       self.assertEqual(tree.roots_with_min_height(), ({'A', 'F'}, 3))

def main():
    unittest.main(verbosity = 3)


if __name__ == '__main__':
    main()
