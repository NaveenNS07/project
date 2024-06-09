s = "abc"
shift = [[0, 1], [1, 2]]
total = 0
for direction, amount in shift:
    if direction == 0:
        total -= amount
    else:
        total += amount
effective_shift = total % len(s)
if effective_shift > 0:
    s = s[-effective_shift:] + s[:-effective_shift]
elif effective_shift < 0:
    s = s[-effective_shift:] + s[:-effective_shift]

print(s)  