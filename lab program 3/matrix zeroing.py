matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]

rows, cols = len(matrix), len(matrix[0])
row_zero = False

for i in range(rows):
    if matrix[i][0] == 0:
        row_zero = True
    for j in range(1, cols):
        if matrix[i][j] == 0:
            matrix[i][0] = matrix[0][j] = 0

for i in range(1, rows):
    for j in range(1, cols):
        if matrix[i][0] == 0 or matrix[0][j] == 0:
            matrix[i][j] = 0

if matrix[0][0] == 0:
    for j in range(cols):
        matrix[0][j] = 0

if row_zero:
    for j in range(rows):
        matrix[j][0] = 0

print(matrix)