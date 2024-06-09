def maxDiff(num):
    s = str(num)
    a = int(s.replace(max(s), '9'))
    b = int(s.replace(min(filter(lambda x: x != '0', s)), '1'))
    return a - b
num = 555
print(maxDiff(num))