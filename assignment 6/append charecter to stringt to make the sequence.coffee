def minCharsToAppend(s: str, t: str) -> int:
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            j += 1
        i += 1
    return len(t) - j

print(minCharsToAppend("coaching", "coding")) 
print(minCharsToAppend("abcde", "a"))  
print(minCharsToAppend("z", "abcde"))  