This pacakge focuses on creating a Graph instance, which takes user's inputs to deal with topics in the Graph Theory.

User's inputs are: 1). edges in a specific graph and 2). edges' corresponding edge_lens in the form of:
  1). edges = ['AB', 'AC', 'BC', 'DE', 'EF', 'FG', 'DG']
  2). edge_lens = [2, 2, 2, 1, 1, 1, 1]
For example, above is the inputs for a DISCONNECTED graph consisting of 
  1). Triangle ABC with side length equals 2 and 
  2). Square DEFG with side length equals 1

The main methods and functions of this package contains four consistent and related parts: 
  1) Check and format user's inputs and report ValueError when the graph cannot be created.
  2) Find all CONNECTED sub_graphs given the input graph.
  3) Find all Cycles in a connected graph. (can be applied interactively with method 2)
  4) Find the Shortest Path and minimum path length between two nodes in the graph

The package applies one self-defined Graph class to take user's inputs and to conduct necessary set and get methods.
A drivers module is also setup with a bunch of functions to support methods mentioned above in the Graph class.
