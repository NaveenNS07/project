def fourSum(nums, target):
    nums.sort()
    results = []
    findNsum(nums, target, 4, [], results)
    return results

def findNsum(nums, target, N, result, results):
    if len(nums) < N or N < 2 or target < nums[0] * N or target > nums[-1] * N:
        return
    if N == 2:
        left, right = 0, len(nums) - 1
        while left < right:
            s = nums[left] + nums[right]
            if s == target:
                results.append(result + [nums[left], nums[right]])
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
            elif s < target:
                left += 1
            else:
                right -= 1
    else:
        for i in range(len(nums) - N + 1):
            if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                findNsum(nums[i + 1:], target - nums[i], N - 1, result + [nums[i]], results)

nums = [1, 0, -1, 0, -2, 2]
target = 0
print(fourSum(nums, target))