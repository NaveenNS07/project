def armstr(num, c):
    if num == 0:
        return 0
    return ((num % 10) ** c) + armstr(num // 10, c)

def check(num):
    c = len(str(num))
    return num == armstr(num, c)

number = int(input("Enter a number: "))
print(check(number))