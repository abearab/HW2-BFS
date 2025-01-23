import igraph as ig
import networkx as nx

from collections import deque

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
            ## use networkx BFS
            # return list(nx.bfs_tree(self.graph, start))

            ## reimplement BFS
            # Source: https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
            # Create a queue for BFS

            adj = self.graph.adj
            result = []

            q = deque()
            
            # Initially mark all the vertices as not visited
            # When we push a vertex into the q, we mark it as visited
            visited = {node: False for node in adj}

            # Mark the source node as visited and enqueue it
            visited[start] = True
            q.append(start)

            # Iterate over the queue
            while q:
            
                # Dequeue a vertex from queue and print it
                curr = q.popleft()
                result.append(curr)

                # Get all adjacent vertices of the dequeued 
                # vertex. If an adjacent has not been visited, 
                # mark it visited and enqueue it
                for x in adj[curr]:
                    if not visited[x]:
                        visited[x] = True
                        q.append(x)

            return result

        elif nx.has_path(self.graph, start, end):
            ## use networkx shortest path
            return nx.shortest_path(self.graph, start, end)

            ## reimplement BFS with pathfinding
            #TODO: write this part from scratch
        
        elif not nx.has_path(self.graph, start, end):
            return None
