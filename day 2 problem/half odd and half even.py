nums = [1, 2, 3, 4, 5, 6]
half = [x for x in nums if x % 2 == 0] + [x for x in nums if x % 2 != 0]
print(half)