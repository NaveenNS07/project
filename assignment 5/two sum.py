def two(nums, target):
    l = {}
    for i, num in enumerate(nums):
        index = target - num
        if index in l:
            return [l[index], i]
        l[num] = i
    return None

nums = [2, 7, 11, 15]
target = 9
result = two(nums, target)
print(result) 
