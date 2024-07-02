import math

def closest(points):
    def distance(p1, p2):
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    def brute(points, n):
        min_dist = float('inf')
        for i in range(n):
            for j in range(i + 1, n):
                if distance(points[i], points[j]) < min_dist:
                    min_dist = distance(points[i], points[j])
        return min_dist

    def closest(px, py, n):
        if n <= 3:
            return brute(px, n)

        mid = n // 2
        mid_point = px[mid]

        pyl = [point for point in py if point[0] < mid_point[0]]
        pyr = [point for point in py if point[0] >= mid_point[0]]

        dl = closest(px, pyl, mid)
        dr = closest(px[mid:], pyr, n - mid)

        d = min(dl, dr)

        strip = [point for point in py if abs(point[0] - mid_point[0]) < d]
        strip.sort(key=lambda x: x[1])

        min_strip = float('inf')
        for i in range(len(strip)):
            j = i + 1
            while j < len(strip) and (strip[j][1] - strip[i][1]) < d:
                min_strip = min(min_strip, distance(strip[i], strip[j]))
                j += 1

        return min(d, min_strip)

    points.sort(key=lambda x: x[0])
    px = points.copy()
    points.sort(key=lambda x: x[1])
    py = points.copy()

    return closest(px, py, len(points))

points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print("The smallest distance is", closest(points))