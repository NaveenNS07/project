def sequentialsearch(arr, target):
    for index, element in enumerate(arr):
        if element == target:
            return index
    return -1

arr = [10, 20, 30, 40, 50]
target = 30

result = sequentialsearch(arr, target)
if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the array")
