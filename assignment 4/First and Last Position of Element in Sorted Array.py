def findFirstPosition(nums, target):
    left, right = 0, len(nums) - 1
    first_position = -1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            first_position = mid
            right = mid - 1  
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return first_position

def findLastPosition(nums, target):
    left, right = 0, len(nums) - 1
    last_position = -1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            last_position = mid
            left = mid + 1  
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return last_position

def searchRange(nums, target):
    first_position = findFirstPosition(nums, target)
    last_position = findLastPosition(nums, target)
    
    return [first_position, last_position]
nums = [5, 7, 7, 8, 8, 10]
target = 8
result = searchRange(nums, target)
print(f"First and last positions of target {target} are: {result}")

target = 6
result = searchRange(nums, target)
print(f"First and last positions of target {target} are: {result}")
