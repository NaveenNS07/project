def min_addition_to_make_beautiful(n, target):
    def sum_of_digits(num):
        return sum(int(digit) for digit in str(num))
    
    if sum_of_digits(n) <= target:
        return 0
    
    x = 0
    increment = 1
    
    while sum_of_digits(n + x) > target:
        next = increment - (n % increment)
        x += next
        n += next
        increment *= 10
    
    return x

n = 467
target = 15
print(min_addition_to_make_beautiful(n, target))  
