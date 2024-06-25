def min_repeating_times(a, b):
    if b in a:
        return 1
    repeated_a = a
    count = 1
    while len(repeated_a) < len(b):
        repeated_a += a
        count += 1
        if len(repeated_a) >= len(b) and b in repeated_a:
            return count
    return -1

a = "abc"
b = "cab"
result = min_repeating_times(a, b)
print(result) 