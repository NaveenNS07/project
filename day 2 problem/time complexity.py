n = 10
print(n)
for i in range(n):
    print(i)

for i in range(n):
    for j in range(n):
        print(i, j)

i = n
while i > 0:
    print(i)
    i = i // 2