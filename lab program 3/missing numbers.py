arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15] 
n = len(arr) + 1
total = n * (n + 1) // 2
missing_number = total - sum(arr)
print("The missing number is:", missing_number)