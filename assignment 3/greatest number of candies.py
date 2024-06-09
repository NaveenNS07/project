candies = [2, 3, 5, 1, 3]
extra = 3

m = max(candies)
result = [candy + extra >= m for candy in candies]

print(result)