n = 5
k = 2

result = 1
for i in range(1, k + 1):
    result = result * (n - i + 1) // i

print(f"The binomial coefficient of {n} choose {k} is: {result}")