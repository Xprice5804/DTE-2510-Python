from WeightedGraph import WeightedGraph

graph = WeightedGraph()
graph.addVertex('U')
graph.addVertex('V')
graph.addVertex('X')
graph.addEdge('U', 'V', 3.5);
graph.addEdge('V', 'U', 3.5);
graph.addEdge('U', 'X', 2.1);
graph.addEdge('X', 'U', 2.1);
graph.addEdge('V', 'X', 3.1);
graph.addEdge('X', 'V', 3.1);
tree = graph.getShortestPath(1)
graph.printWeightedEdges()
tree.printTree()