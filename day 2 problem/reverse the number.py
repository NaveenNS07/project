def reverse(n, rev=0):
    if n == 0:
        return rev
    else:
        return reverse(n // 10, rev * 10 + n % 10)

number = 12345
n = reverse(number)
print(f"The reversed number of {number} is: {n}")