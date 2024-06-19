def minOperations(nums):
    operations = 0
    for i in range(1, nums.length):
        if nums[i] <= nums[i - 1]:
            increment = nums[i - 1] - nums[i] + 1
            nums[i] += increment
            operations += increment
    return operations

nums = [1, 2, 3, 4]
print(minOperations(nums)) 
