# Start 'A' End 'G'

import heapq as hq

graph = {
    'A': {'B': 3, 'C': 3},
    'B': {'A': 3, 'D': 3.5, 'E': 2.8, 'G':4},
    'C': {'A': 3, 'E': 2.7, 'F': 3.5},
    'D': {'B': 3.5, 'E': 3.1, 'G': 10},
    'E': {'B': 2.8, 'C': 2.7, 'D': 3.1, 'G': 7},
    'F': {'G': 1, 'C': 3.5},
    'G': {'F': 1, 'E': 7, 'D': 10}
}

def ted_dk(graph, START, END):
    trace_route = {node:"" for node in graph}
    pq = []
    distance = {node:float('inf') for node in graph}
    distance[START] = 0
    hq.heappush(pq, (0, START))

    while len(pq) >0:
        from_node = hq.heappop(pq)

        if from_node[1] == END:
            return distance, trace_route

        for to_node in graph[from_node[1]]:
            if(distance[to_node] > graph[from_node[1]][to_node]+distance[from_node[1]]):
                distance[to_node] = graph[from_node[1]][to_node]+distance[from_node[1]]
                hq.heappush(pq, (graph[from_node[1]][to_node], to_node))
                trace_route += from_node[1] + '->' + to_node 


a, b = ted_dk(graph, 'A', 'G')
print(f"distance={a}, route={b}")