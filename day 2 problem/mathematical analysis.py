def non(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
def recursive(n):
    if n == 0:
        return 1
    else:
        return n * recursive(n - 1)
number = 5
nonresult = non(number)
result = recursive(number)
print(f"Non-Recursive Factorial of {number}: {nonresult}")
print(f"Recursive Factorial of {number}: {result}")