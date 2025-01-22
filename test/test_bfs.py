# write tests for bfs
import pytest
import networkx as nx
from search import graph

def test_bfs_traversal():
    """
    unit test for a breadth-first traversal
    
    Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    g = graph.Graph('data/tiny_network.adjlist')

    start_node = 'Hani Goodarzi'
    end_node = 'Luke Gilbert'
    n_nodes = g.graph.number_of_nodes()

    ## check right number of nodes
    assert len(g.bfs(start=start_node)) == n_nodes
    assert len(g.bfs(start=start_node, end=end_node)) <= n_nodes

    ## check right order of nodes
    bfs_orders = [v for _,v in dict(nx.single_source_shortest_path_length(g.graph, start_node)).items()]
    assert bfs_orders == sorted(bfs_orders)

    ## check right order of nodes in other case
    subgraph = g.graph.subgraph(g.bfs(start=start_node, end=end_node))
    bfs_orders_subgraph = [v for _,v in dict(nx.single_source_shortest_path_length(subgraph, start_node)).items()]
    assert bfs_orders_subgraph == sorted(bfs_orders_subgraph)


def test_bfs():
    """unit test for your breadth-first search
    
    This code generates an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them. Then, there is 
    additional test for nodes that are not connected 
    which should return None. 
    """
    g = graph.Graph('data/citation_network.adjlist')

    start_node = 'Tony Capra'
    end_node = 'Katie Pollard'

    ## check if nodes that are connected return a (shortest) path between them
    assert g.bfs(start=start_node, end=end_node) == nx.shortest_path(g.graph, start_node, end_node)

    ## test for nodes that are not connected which should return None.
    # find a node that is not connected to start_node
    for node in g.graph.nodes:
        if ' ' not in node:
            continue
        elif not nx.has_path(g.graph, start_node, node):
            break
    
    assert g.bfs(start=start_node, end=node) == None
