def minOperations(nums):
    count = 0
    for i in range(len(nums)):
        if nums[i] != 0 and nums[i] != i:
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
            count += 1
    return count

nums = [4, 2, 0, 3, 1]
print(minOperations(nums)) 