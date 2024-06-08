def romanToInt(s):
    r = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev = 0

    for char in s:
        value = r[char]
        result += value
        if value > prev:
            result -= 2 * prev
        prev = value

    return result

print(romanToInt("XXVII"))