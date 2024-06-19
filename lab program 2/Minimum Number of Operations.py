def min_operations(arr1, arr2):
    n, m = len(arr1), len(arr2)
    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if arr1[i - 1] > dp[i - 1][j - 1]:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])
            if arr2[j - 1] > dp[i - 1][j - 1]:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + 1)

    ans = min(dp[n])
    return ans if ans != float('inf') else -1

arr1 = [1, 5, 3, 6, 7]
arr2 = [1, 3, 2, 4]
output = min_operations(arr1, arr2)
print(output)