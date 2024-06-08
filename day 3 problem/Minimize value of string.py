def minimizeCost(s):
    res = []
    l = {}
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    for char in s:
        if char == '?':
            min = None
            m = float('inf')
            
            for letter in alphabet:
                cost = l.get(letter, 0)
                if cost < m:
                    m = cost
                    min = letter
            
            res.append(min)
            l[min] = l.get(min, 0) + 1
        else:
            res.append(char)
            l[char] = l.get(char, 0) + 1
    
    return ''.join(res)

s = "a?b?c?"
print(minimizeCost(s))