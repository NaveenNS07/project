def count(arr):
    return sum(1 for x in arr if x + 1 in arr)

arr = [1, 2, 3]
print(count(arr))