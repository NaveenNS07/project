def bellman_ford(graph, source):
    vertices = graph.keys()
    distances = {vertex: float('infinity') for vertex in vertices}
    distances[source] = 0

    for _ in range(len(vertices) - 1):
        for u in vertices:
            for v, weight in graph[u].items():
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight

    for u in vertices:
        for v, weight in graph[u].items():
            if distances[u] + weight < distances[v]:
                print("Graph contains negative weight cycle")
                return

    print("Shortest distances from the source:")
    for vertex, distance in distances.items():
        print(f"Source -> {vertex}: Distance = {distance}")

graph = {
    'A': {'B': -1, 'C': 4},
    'B': {'C': 3, 'D': 2, 'E': 2},
    'C': {},
    'D': {'B': 1, 'C': 5},
    'E': {'D': -3}
}

source_vertex = 'A'

bellman_ford(graph, source_vertex)