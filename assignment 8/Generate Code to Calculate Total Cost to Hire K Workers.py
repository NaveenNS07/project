import heapq

def mincostToHireWorkers(costs, k, candidates):
    n = len(costs)
    cost_ratio = sorted([(costs[i] / float(wage), costs[i]) for i, wage in enumerate(costs)])
    heap = []
    total_cost = float('inf')
    sum_costs = 0

    for ratio, cost in cost_ratio:
        heapq.heappush(heap, -cost)
        sum_costs += cost

        if len(heap) > candidates:
            sum_costs += heapq.heappop(heap)

        if len(heap) == candidates:
            total_cost = min(total_cost, ratio * sum_costs)

    return int(total_cost)

costs = [17, 12, 10, 2, 7, 2, 11, 20, 8]
k = 3
candidates = 4
output = mincostToHireWorkers(costs, k, candidates)
print(output) 