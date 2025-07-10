import sys
import heapq

graph = {
    'A': {'B': 3, 'C': 3},
    'B': {'A': 3, 'D': 3.5, 'E': 2.8},
    'C': {'A': 3, 'E': 2.7, 'F': 3.5},
    'D': {'B': 3.5, 'E': 3.1, 'G': 10},
    'E': {'B': 2.8, 'C': 2.7, 'D': 3.1, 'G': 7},
    'F': {'G': 2.5, 'C': 3.5},
    'G': {'F': 2.5, 'E': 7, 'D': 10}
}

# have to use tuple to use heapq cause of ordering using first element of tuple
def dijkstra(graph, start , end):
    pq = []
    heapq.heappush(pq, (0, start))
    distance = {node:float('infinity') for node in graph}
    distance[start] = 0
    trace_route = {node: start for node in graph}
    
    while len(pq) > 0:
        src_weight, src_node = heapq.heappop(pq)

        if src_node == end:
            break
        
        if src_weight > distance[src_node]:
            continue

        for tgt_node, tgt_weight in graph[src_node].items():
            compare_dis = src_weight + tgt_weight
            if(compare_dis < distance[tgt_node]):
                distance[tgt_node] = compare_dis
                trace_route[tgt_node] = trace_route[src_node] + ' -> ' + tgt_node
                heapq.heappush(pq, (compare_dis, tgt_node))


    size = sys.getsizeof(trace_route)
    print(f"size={size} bytes")
    return trace_route[end], distance[end], distance

# Find shortest path from B to F
# distance, path = dijkstra(graph, 'B','F')
trace_route , distance, distance2= dijkstra(graph, 'A','G')
print(f"Shortest distance: {distance}")
print(f"Path: {trace_route}")
print(distance2)