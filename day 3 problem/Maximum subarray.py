def maxSubArray(nums):
    current = g = nums[0]
    
    for num in nums[1:]:
        current = max(num, current + num)
        if current > g:
            g = current
    
    return g

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums)) 