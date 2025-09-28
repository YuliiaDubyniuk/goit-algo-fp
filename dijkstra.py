import networkx as nx
import matplotlib.pyplot as plt
import heapq


def dijkstra(graph, start):
    """
    Returns a dictionary with the shortest distances from the start vertex
    to all other vertices in the graph.
    """
    # initialize distances
    distances = {node: float('inf') for node in graph.nodes()}
    distances[start] = 0

    # initialize min-heap
    heap = [(0, start)]

    while heap:
        current_distance, current_node = heapq.heappop(heap)
        if current_distance > distances[current_node]:
            continue

        # check all neighbors of the current node
        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']
            distance_via_current = current_distance + weight

            # if we found a shorter path to neighbor, update and push into heap
            if distance_via_current < distances[neighbor]:
                distances[neighbor] = distance_via_current
                heapq.heappush(heap, (distance_via_current, neighbor))
    return distances


if __name__ == "__main__":
    # creating Graph
    g = nx.Graph()
    g.add_edge('A', 'B', weight=3)
    g.add_edge('A', 'C', weight=11)
    g.add_edge('B', 'D', weight=5)
    g.add_edge('C', 'D', weight=4)
    g.add_edge('D', 'E', weight=9)

    start_node = 'A'
    shortest_paths = dijkstra(g, start_node)

    print(f"Shortest distances from node {start_node}:")
    for node, distance in shortest_paths.items():
        print(f"{start_node} -> {node}: {distance}")
