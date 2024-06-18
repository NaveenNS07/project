def maxSumOfDistinctSubarrays(nums, k):
    if len(set(nums)) < k:
        return 0
    max_sum = 0
    for i in range(len(nums) - k + 1):
        if len(set(nums[i:i+k])) == k:
            max_sum = max(max_sum, sum(nums[i:i+k]))
    return max_sum

nums1 = [1, 5, 4, 2, 9, 9, 9]
k1 = 3
print(maxSumOfDistinctSubarrays(nums1, k1))  

nums2 = [4, 4, 4]
k2 = 3
print(maxSumOfDistinctSubarrays(nums2, k2))  