def meet_in_middle(arr, target):
    n = len(arr)
    result = []
    for i in range(1 << n):
        subset = [arr[j] for j in range(n) if (i & (1 << j))]
        if sum(subset) == target:
            result.append(subset)
    return result

arr = [1, 3, 4, 2, 2]
target = 5
print(meet_in_middle(arr, target))