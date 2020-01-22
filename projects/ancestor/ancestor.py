import sys

sys.path.append("../graph")
from graph import Graph
from util import Stack, Queue


def earliest_ancestor(ancestors, starting_node):
    # build the graph. the shortest path to the "oldest" node
    graph = Graph()
    for pair in ancestors:
        parent, child = [i for i in pair]
        graph.add_vertex(parent)
        graph.add_vertex(child)
        graph.add_edge(child, parent)
    # BFS - shortest path, use a queue
    q = Queue()
    # building a path, not just nodes
    q.enqueue([starting_node])
    # longest path found so far
    max_path_len = 1
    # earliest ancestor var, default -1
    earliest_ancestor = -1
    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]
        # if found a new candidate set it as earliest
        if (len(path) >= max_path_len and v < earliest_ancestor) or (len(path) > max_path_len):
            earliest_ancestor = v
            max_path_len = len(path)
        # loop through graph
        for neighbor in graph.vertices[v]:
            path_copy = list(path)
            path_copy.append(neighbor)
            q.enqueue(path_copy)
    return earliest_ancestor


ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

bob = earliest_ancestor(ancestors, 3)
# print(bob.vertices)
print(bob == 10)
