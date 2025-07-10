import heapq
import sys

def dijkstra(graph, start, end):
    # Initialize distances and predecessors
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    predecessors = {node: None for node in graph}
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Early exit if we reach the target node
        if current_node == end:
            break
            
        if current_distance > distances[current_node]:
            continue
            
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
    
    # Reconstruct path
    path = []
    current = end
    while current:
        path.append(current)
        current = predecessors[current]

    size = sys.getsizeof(path)
    print(f"size={size} bytes")

    path.reverse()
    
    return distances[end], path if path[0] == start else []

# Example graph
graph = {
    'A': {'B': 3, 'C': 3},
    'B': {'A': 3, 'D': 3.5, 'E': 2.8},
    'C': {'A': 3, 'E': 2.8, 'F': 3.5},
    'D': {'B': 3.5, 'E': 3.1, 'G': 10},
    'E': {'B': 2.8, 'C': 2.8, 'D': 3.1, 'G': 7},
    'F': {'G': 2.5, 'C': 3.5},
    'G': {'F': 2.5, 'E': 7, 'D': 10}
}

# Find shortest path from B to F
distance, path = dijkstra(graph, 'B', 'F')
print(f"Shortest distance: {distance}")
print(f"Path: {' → '.join(path)}")
