from itertools import product

def letterCombinations(digits):
    if not digits:
        return []
    
    phone = {'2': ['a', 'b', 'c'],
             '3': ['d', 'e', 'f'],
             '4': ['g', 'h', 'i'],
             '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'],
             '7': ['p', 'q', 'r', 's'],
             '8': ['t', 'u', 'v'],
             '9': ['w', 'x', 'y', 'z']}
    
    return [''.join(p) for p in product(*(phone[d] for d in digits))]

digits = "23"
print(letterCombinations(digits))