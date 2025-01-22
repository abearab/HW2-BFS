import igraph as ig
import networkx as nx

class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def to_igraph(self):
        """
        Convert networkx graph to igraph graph
        """
        G = ig.Graph(directed=True)
        G.add_vertices(list(self.graph.nodes))
        G.add_edges(list(self.graph.edges))
        return G
    
    def bfs(self, start, end=None):
        """
        perform a breadth first traversal and pathfinding on graph G

        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None

        """
        if end is None:
            return list(nx.bfs_tree(self.graph, start))
        elif nx.has_path(self.graph, start, end):
            return nx.shortest_path(self.graph, start, end)
        elif not nx.has_path(self.graph, start, end):
            return None
