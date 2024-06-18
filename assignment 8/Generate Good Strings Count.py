def count_good_strings(low, high, zero, one):
    MOD = 10**9 + 7
    dp = [[[0] * 2 for _ in range(high + 1)] for _ in range(2)]
    dp[0][0][0] = dp[0][0][1] = dp[1][0][0] = dp[1][0][1] = 1
    
    for i in range(1, high + 1):
        for j in range(1, 2):
            for k in range(2):
                dp[j][i][k] = (dp[j][i][k] + dp[j][i - 1][k]) % MOD
                if k == 0:
                    dp[j][i][1] = (dp[j][i][1] + dp[j - 1][i - 1][k]) % MOD
                else:
                    dp[j][i][0] = (dp[j][i][0] + dp[j - 1][i - 1][k]) % MOD
    
    result = 0
    for i in range(low, high + 1):
        result = (result + sum(dp[0][i]) + sum(dp[1][i])) % MOD
    
    return result

low = 3
high = 3
zero = 1
one = 1
output = count_good_strings(low, high, zero, one)
print(output)