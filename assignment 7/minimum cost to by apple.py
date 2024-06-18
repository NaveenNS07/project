from collections import defaultdict
import heapq

def minCostToBuyApples(n, roads, appleCost, k):
    graph = defaultdict(list)
    for a, b, cost in roads:
        graph[a].append((b, cost))
        graph[b].append((a, cost))

    def dijkstra(start):
        heap = [(0, start)]
        costs = [float('inf')] * (n + 1)
        costs[start] = 0

        while heap:
            curr_cost, node = heapq.heappop(heap)
            if curr_cost > costs[node]:
                continue

            for neighbor, road_cost in graph[node]:
                new_cost = curr_cost + road_cost
                if new_cost < costs[neighbor]:
                    costs[neighbor] = new_cost
                    heapq.heappush(heap, (new_cost, neighbor))

        return [cost * k for cost in costs[1:]]

    return dijkstra(1)

n = 4
roads = [[1, 2, 4], [2, 3, 2], [2, 4, 5], [3, 4, 1], [1, 3, 4]]
appleCost = [56, 42, 102, 301]
k = 2
output = minCostToBuyApples(n, roads, appleCost, k)
print(output)