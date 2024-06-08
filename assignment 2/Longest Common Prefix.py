def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    shortest = min(strs, key=len)
    
    for i, char in enumerate(shortest):
        for other in strs:
            if other[i] != char:
                return shortest[:i]
    
    return shortest