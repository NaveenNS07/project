import heapq

def dijkstra(n, graph, source):
    distances = [float('inf')] * n
    distances[source] = 0
    p = [(0, source)]  
    
    while p:
        c, v = heapq.heappop(p)
        
        if c > distances[v]:
            continue
        
        for neighbor in range(n):
            weight = graph[v][neighbor]
            if weight != float('inf'):  
                distance = c + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(p, (distance, neighbor))
    
    return distances

n = 5
graph = [
    [0, 10, 3, float('inf'), float('inf')],
    [float('inf'), 0, 1, 2, float('inf')],
    [float('inf'), 4, 0, 8, 2],
    [float('inf'), float('inf'), float('inf'), 0, 7],
    [float('inf'), float('inf'), float('inf'), 9, 0]
]
source = 0
output = dijkstra(n, graph, source)
print(output)  