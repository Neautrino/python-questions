# Maximum Flow and Minimum Cut (Ford-Fulkerson Algorithm)
# Problem Statement: Given a flow network with capacities on edges, find the maximum flow from a source node to a sink node while minimizing the cut's capacity.

# Sample Input: A graph with capacities represented as an adjacency matrix.
graph = [
    [0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0]
]

# Ford-Fulkerson algorithm for finding the maximum flow in a flow network.
from collections import deque

def ford_fulkerson(graph, source, sink):
    def dfs(graph, source, sink, parent):
        visited[source] = True
        for node, capacity in enumerate(graph[source]):
            if not visited[node] and capacity > 0:
                parent[node] = source
                if node == sink:
                    return True
                if dfs(graph, node, sink, parent):
                    return True
        return False

    max_flow = 0
    parent = [-1] * len(graph)

    while dfs(graph, source, sink, parent):
        path_flow = float('inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]
        max_flow += path_flow

        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]

        visited = [False] * len(graph)

    return max_flow

# Find and print the maximum flow in the network.
source, sink = 0, 5
max_flow = ford_fulkerson(graph, source, sink)
print("Maximum Flow:", max_flow)
