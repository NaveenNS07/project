def checkIfCanBreak(s1, s2):
    return all(x >= y for x, y in zip(sorted(s1), sorted(s2)))

s1 = "abc"
s2 = "xya"
print(checkIfCanBreak(s1, s2))