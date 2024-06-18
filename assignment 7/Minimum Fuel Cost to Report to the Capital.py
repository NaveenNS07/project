from collections import defaultdict

def minFuel(roads, seats):
    graph = defaultdict(list)
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
    
    def dfs(node, parent):
        total_seats = seats
        for neighbor in graph[node]:
            if neighbor != parent:
                total_seats += dfs(neighbor, node)
        return total_seats - 1
    
    return dfs(0, -1)

roads = [[0,1],[0,2],[0,3]]
seats = 5
print(minFuel(roads, seats))