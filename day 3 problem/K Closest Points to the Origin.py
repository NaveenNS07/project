import heapq

def kClosest(points, k):
    return heapq.nsmallest(k, points, key=lambda x: x[0]**2 + x[1]**2)


points = [[1, 3], [-2, 2], [5, 8], [0, 1]]
k = 2
print(kClosest(points, k))  