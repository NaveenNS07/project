def findPivotInteger(n: int) -> int:
    total_sum = (n * (n + 1)) // 2  
    left_sum = 0
    
    for x in range(1, n + 1):
        left_sum += x
        right_sum = total_sum - left_sum
        if left_sum == right_sum:
            return x
    
    return -1

print(findPivotInteger(8))
print(findPivotInteger(1))  
print(findPivotInteger(4)) 