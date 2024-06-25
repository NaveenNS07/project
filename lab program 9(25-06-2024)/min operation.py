def min_operations(arr1, arr2):
    n = len(arr1)
    dp = [-1] * n
    dp[0] = 0 if arr1[0] < arr2[0] else 1

    for i in range(1, n):
        if arr1[i] > arr1[i - 1]:
            dp[i] = dp[i - 1]
        min_ops = float('inf')
        for j in range(len(arr2)):
            if arr2[j] < arr1[i]:
                if dp[i - 1] != -1:
                    min_ops = min(min_ops, dp[i - 1] + 1)
        if min_ops != float('inf'):
            dp[i] = min_ops

    return dp[-1]

arr1 = [1, 5, 3, 6, 7]
arr2 = [1, 3, 2, 4]
print(min_operations(arr1, arr2))  
