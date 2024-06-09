from typing import List

class BinaryMatrix:
    def dimensions(self):
        pass
    
    def get(self, row: int, col: int) -> int:
        pass

def leftMostColumnWithOne(binaryMatrix: BinaryMatrix) -> int:
    rows, cols = binaryMatrix.dimensions()
    rows = 0
    col = cols - 1
    while rows < rows and col >= 0:
        if binaryMatrix.get(rows, col) == 1:
            col -= 1
        else:
            rows += 1
    return col + 1 if col != cols - 1 else -1
if __name__ == "__main__":
     class ExampleBinaryMatrix(BinaryMatrix):
        def dimensions(self):
            return 3, 3
        
        def get(self, row: int, col: int) -> int:
            matrix = [
                [0, 0, 0],
                [0, 1, 1],
                [0, 0, 1]
            ]
            return matrix[row][col]
binaryMatrix = ExampleBinaryMatrix()
result = leftMostColumnWithOne(binaryMatrix)
print(result)  