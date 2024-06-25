def generate_max_local(grid):
    n = len(grid)
    max_local = [[0] * (n - 2) for _ in range(n - 2)]
    
    for i in range(n - 2):
        for j in range(n - 2):
            submatrix = [grid[x][j:j+3] for x in range(i, i+3)]
            max_local[i][j] = max([max(row) for row in submatrix])
    
    return max_local

grid = [[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]
result = generate_max_local(grid)
print(result)
