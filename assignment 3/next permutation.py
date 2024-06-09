nums = [1, 2, 3]
i = len(nums) - 2
while i >= 0 and nums[i + 1] <= nums[i]:
    i -= 1

if i >= 0:
    j = len(nums) - 1
    while j >= 0 and nums[j] <= nums[i]:
        j -= 1
    nums[i], nums[j] = nums[j], nums[i]

nums[i + 1:] = nums[i + 1:][::-1]

print(nums) 