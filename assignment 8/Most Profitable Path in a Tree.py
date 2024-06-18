from collections import defaultdict

def maxProfitablePath(edges, bob, amount):
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    def dfs(node, parent):
        nonlocal max_profit
        if amount[node] > 0:
            max_profit += amount[node]
        for neighbor in graph[node]:
            if neighbor != parent:
                max_profit_neighbor = max(0, dfs(neighbor, node))
                if amount[node] < 0:
                    max_profit += max_profit_neighbor
                else:
                    max_profit += max_profit_neighbor / 2
        return max_profit

    max_profit = 0
    return dfs(bob, -1)

edges = [[0,1],[1,2],[1,3],[3,4]]
bob = 3
amount = [-2,4,2,-4,6]
print(maxProfitablePath(edges, bob, amount))