def length(s):
    start = 0
    m = 0
    index = {}

    for end in range(len(s)):
        if s[end] in index:
            start = max(start, index[s[end]] + 1)

        index[s[end]] = end
        m = max(m, end - start + 1)

    return m

s = "abindexabindexbb"
print(length(s))  

