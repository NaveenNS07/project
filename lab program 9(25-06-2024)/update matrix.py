from collections import deque

def updateMatrix(mat):
    queue = deque()
    rows, cols = len(mat), len(mat[0])
    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 0:
                queue.append((i, j))
            else:
                mat[i][j] = float('inf')
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and mat[nx][ny] > mat[x][y] + 1:
                mat[nx][ny] = mat[x][y] + 1
                queue.append((nx, ny))
    
    return mat

mat = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
result = updateMatrix(mat)
print(result)
