def is_perfect_number(n):
    if n < 1:
        return False
    sum1 = sum(i for i in range(1, n) if n % i == 0)
    return sum1 == n

number = int(input("Enter a number: "))
print(f"Is {number} a perfect number? {is_perfect_number(number)}")