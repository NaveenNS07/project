x = -123
if x < 0:
    rev = int(str(x)[0] + str(x)[:0:-1])
else:
    rev = int(str(x)[::-1])

if rev < -2**31 or rev > 2**31 - 1:
    print(0)
else:
    print(rev)