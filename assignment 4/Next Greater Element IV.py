def second_greater_element(nums):
    result = [-1] * len(nums)
    
    for i in range(len(nums)):
        first = False
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i]:
                if not first:
                    first = True
                else:
                    result[i] = nums[j]
                    break

    return result

nums = [1, 2, 4, 3]
print(second_greater_element(nums)) 
