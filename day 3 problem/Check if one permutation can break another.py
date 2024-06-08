def checkIfCanBreak(s1, s2):
    s1_sorted = sorted(s1)
    s2_sorted = sorted(s2)
    
    def can_break(x, y):
        return all(x[i] >= y[i] for i in range(len(x)))
    
    return can_break(s1_sorted, s2_sorted) or can_break(s2_sorted, s1_sorted)

s1 = "abc"
s2 = "xya"
print(checkIfCanBreak(s1, s2))