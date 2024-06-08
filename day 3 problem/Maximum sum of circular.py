def maxSubArray(nums):
    c = g = nums[0]
    for num in nums[1:]:
        c = max(num, c + num)
        if c > g:
            g = c
    return g

def maxSubarraySumCircular(nums):
    total = sum(nums)
    max_kadane = maxSubArray(nums)
    min_kadane = -maxSubArray([-num for num in nums])
    
    if min_kadane == total:
        return max_kadane
    
    return max(max_kadane, total + min_kadane)

nums = [1, -2, 3, -2]
print(maxSubarraySumCircular(nums))