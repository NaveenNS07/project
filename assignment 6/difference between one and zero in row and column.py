def earliestClosingHour(customers: str) -> int:
    n = len(customers)
    min_penalty = float('inf')
    min_hour = 0
    
    for hour in range(n + 1):
        penalty = 0
        for i in range(n):
            if hour == i and customers[i] == 'N':
                penalty += 1 
            elif hour != i and customers[i] == 'Y':
                penalty += 1 
        if penalty < min_penalty:
            min_penalty = penalty
            min_hour = hour
    
    return min_hour

print(earliestClosingHour("YYNY"))  
print(earliestClosingHour("NNNNN"))  
print(earliestClosingHour("YYYY"))