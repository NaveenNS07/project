def countPalindromicSubsequences(s: str) -> int:
    MOD = 10**9 + 7
    n = len(s)
    dp = [[0] * 10 for _ in range(n)]
    
    for i in range(n):
        dp[i][int(s[i])] = 1
    
    for i in range(1, n):
        for j in range(10):
            for k in range(10):
                if s[i] == str(k):
                    dp[i][j] += dp[i-1][k]
                    dp[i][j] %= MOD
    
    return sum(dp[-1]) % MOD

print(countPalindromicSubsequences("103301"))  
print(countPalindromicSubsequences("0000000"))  
print(countPalindromicSubsequences("9999900000"))