def sortColors(nums):
    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[high], nums[mid] = nums[mid], nums[high]
            high -= 1
nums = [2, 0, 2, 1, 1, 0]
sortColors(nums)
print(f"Sorted colors: {nums}")

nums = [2, 0, 1]
sortColors(nums)
print(f"Sorted colors: {nums}")
