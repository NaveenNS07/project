def graphcolour(graph):
    n = len(graph)
    result = [-1] * n 
    result[0] = 0  

    available = [False] * n

    for u in range(1, n):
        for i in range(n):
            if graph[u][i] != 0 and result[i] != -1:
                available[result[i]] = True

        cr = 0
        while cr < n and available[cr]:
            cr += 1
        result[u] = cr

        for i in range(n):
            if graph[u][i] != 0 and result[i] != -1:
                available[result[i]] = False

    return result

graph = [(0,1),(1,2),(2,3),(3,0),(0,2)]

coloring = graphcolour(graph)
print("Assigned colors:", coloring)
