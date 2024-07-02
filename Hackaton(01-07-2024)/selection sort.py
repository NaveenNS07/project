def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        m = i
        for j in range(i+1, n):
            if arr[j] < arr[m]:
                m = j
                arr[i], arr[m] = arr[m], arr[i]
    return arr
random = [5, 2, 9, 1, 5, 6]
sorted = selection_sort(random)
print("Random Array Sorted:", sorted)
reverse = [10, 8, 6, 4, 2]
r = selection_sort(reverse)
print("Reverse Sorted Array Sorted:", r)
already = [1, 2, 3, 4, 5]
a = selection_sort(already)
print("Already Sorted Array Sorted:", a)
