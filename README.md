# Graph

## Description

The Graph is a package offering solutions to applied graph theory problems and visualizing tree graphs 
in an interactive way.
The package takes in two parameters: a list of edges and a list of corresponding edge lengths such as

* edges = ['AB', 'AC', 'BC', 'DE', 'EF', 'FG', 'DG']
* edge_lens = [2, 2, 2, 1, 1, 1, 1]

It can be used in daily application of graph theory topics such as finding the shortest path in a road 
or a network, checking if a network is connected or not and how reliable a local network is by checking 
how many cycles it contains.
It solves problems including: 
* 1). Test user’s inputs.
* 2). Check connectivity of graph. 
* 3).Find all unique cycles in a graph. 
* 4). Find the shortest path between two input vertices.
* 5). Check if the input graph or any subgraph is a tree. 
If the graph is a tree. Problems that can be solved are: 
* 1). Find optical roots that give the tree a minimum height. 
* 2). Find given node’s parent, children, siblings, ascendents and descendants. 
* 3). Find nodes at the same level. 
* 4). Visualize the tree graph.

## Structure
```Shell
├── Darray
    ├── Darray
        ├── __init__.py
        ├── utils.py
        ├── darray.py
           ├── self.data
           ├── self.colnames
           ├── __init__()
           ├── __str__()
           ├── __getitem__()
           ├── __setitem__()
           ├── __add__() etc...
           ├── order()
           ├── deletena() etc...
           ├── concat_rows() etc...
           ├── summary()
           ├── ...
           
    ├── README.md   
    ├── setup.py
    ├── test.csv
    ├── test.py
```
### Dependencies

* Describe any prerequisites, libraries, OS version, etc., needed before installing program.
* ex. Windows 10

### Installing

* How/where to download your program
* Any modifications needed to be made to files/folders

### Executing program

* How to run the program
* Step-by-step bullets
```
code blocks for commands
```

## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors

Contributors names and contact info

ex. Dominique Pizzie  
ex. [@DomPizzie](https://twitter.com/dompizzie)

## Version History

* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)