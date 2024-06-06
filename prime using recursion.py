def prime(n, i=2):
    if n == i:
        return True
    elif n % i == 0:
        return False
    return prime(n, i + 1)


n = 7
if prime(n):
    print(n, "is Prime")
else:
    print(n, "is not a Prime")