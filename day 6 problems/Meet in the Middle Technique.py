arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 13

n = len(arr)
half = n // 2

left_half = arr[:half]
right_half = arr[half:]

for i in range(1 << half):
    subset_sum = sum(left_half[j] for j in range(half) if (i & (1 << j)) > 0)
    if subset_sum == target:
        print("Found a subset that sums to the target in the left half.")
        break

for i in range(1 << (n - half)):
    subset_sum = sum(right_half[j] for j in range(n - half) if (i & (1 << j)) > 0)
    if subset_sum == target:
        print("Found a subset that sums to the target in the right half.")
        break