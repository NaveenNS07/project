s = "applepenapple"
wordDict = ["apple", "pen"]

dp = [False] * (len(s) + 1)
dp[0] = True

for i in range(1, len(s) + 1):
    for j in range(i):
        if dp[j] and s[j:i] in wordDict:
            dp[i] = True
            break

print(dp[len(s)])