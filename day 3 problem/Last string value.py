def lastStringBeforeEmptying(s):
    while True:
        new_s = list(s)
        for c in 'abcdefghijklmnopqrstuvwxyz':
            if c in new_s:
                new_s.remove(c)
        new_s = ''.join(new_s)
        if new_s == s:
            return s
        s = new_s

s = "aabcbbca"
print(lastStringBeforeEmptying(s))