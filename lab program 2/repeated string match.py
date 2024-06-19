def repeated_string_match(a, b):
    if b in a:
        return 1
    for i in range(1, len(b) // len(a) + 3):
        if b in a * i:
            return i
    return -1

a = "abcd"
b = "cdabcdab"
output = repeated_string_match(a, b)
print(output)