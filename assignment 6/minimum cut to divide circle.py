def minimumCuts(n):
    if n == 1:
        return 0
    elif n % 2 == 0:
        return n // 2
    else:
        return n

if __name__ == "__main__":
    test_cases = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for n in test_cases:
        print(f"Minimum cuts to divide the circle into {n} equal slices: {minimumCuts(n)}")