from path_algo import *
# Example graph represented as an adjacency dictionary
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
graph2 = {
    0: {1: 33, 25: 48},
    1: {0: 33, 26: 48, 2: 43},
    2: {1: 43, 3: 24, 5: 25},
    3: {2: 24, 4: 24, 6: 25},
    4: {24: 24, 7: 35, 22: 48, 26: 43},
    5: {2: 25, 6: 24, 8: 9},
    
}
graph3 = {
    0: {1: 33, 25: 48},
    1: {0: 33, 26: 48},
    25: {0: 48, 26: 33},
    26: {1: 48, 25: 33}
}
start_node = 0
end_node = 26
shortest_distance, shortest_path = dijkstra(graph3, start_node, end_node)
print("Shortest distance from node", start_node, "to node", end_node, ":", shortest_distance)
print("Shortest path:", shortest_path)