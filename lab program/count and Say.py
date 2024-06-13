def countAndSay(n: int) -> str:
    if n == 1:
        return "1"
    
    previous_term = countAndSay(n - 1)
    
    result = ""
    i = 0
    length = len(previous_term)
    
    while i < length:
        count = 1
        while i + 1 < length and previous_term[i] == previous_term[i + 1]:
            i += 1
            count += 1
        
        result += str(count) + previous_term[i]
        i += 1
    return result

n = 5
print(f"The {n}-th term in the count-and-say sequence is: {countAndSay(n)}")
