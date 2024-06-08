def threeSumClosest(nums, target):
    nums.sort()
    closest = float('inf')
    
    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            c = nums[i] + nums[left] + nums[right]
            
            if abs(target - c) < abs(target - closest):
                closest = c
            
            if c < target:
                left += 1
            elif c > target:
                right -= 1
            else:
                return c
                
    return closest
nums = [-1, 2, 1, -4]
target = 1
result = threeSumClosest(nums, target)
print(result)