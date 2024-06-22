def countGoodStrings(n, s1, s2, evil):
    MOD = 10**9 + 7
    dp = [[[0] * 2 for _ in range(len(evil) + 1)] for _ in range(n + 1)]
    dp[0][0][0] = 1

    for i in range(1, n + 1):
        for j in range(len(evil) + 1):
            for k in range(2):
                for x in range(ord(s1[i - 1]) if k == 0 else ord('a'), ord(s2[i - 1]) + 1 if k == 1 else ord('z') + 1):
                    ni, nj, nk = i, j, k
                    while nj and evil[nj - 1] != chr(x):
                        nj = dp[ni][nj][nk]
                    if evil[nj] == chr(x):
                        nj += 1
                    if nj == len(evil):
                        continue
                    if chr(x) == s1[i - 1]:
                        nk = 1
                    dp[i][nj][nk] += dp[i - 1][j][k]
                    dp[i][nj][nk] %= MOD

    ans = sum(sum(dp[n][j][k] for k in range(2)) % MOD for j in range(len(evil) + 1)) % MOD
    return ans

n = 2
s1 = "aa"
s2 = "da"
evil = "b"
output = countGoodStrings(n, s1, s2, evil)
print(output)