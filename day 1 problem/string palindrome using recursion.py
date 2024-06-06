n = 'hari hara'

def palin(n):
    n = n.lower().replace(' ', '')
    return n == n[::-1]

print(palin(n))