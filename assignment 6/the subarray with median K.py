def countSubarraysWithMedianK(nums, k):
    n = len(nums)
    k_index = nums.index(k)

    balance_count = {0: 1}
    balance = 0
    count = 0
    
    for i in range(n):
        if nums[i] > k:
            balance += 1
        elif nums[i] < k:
            balance -= 1
        
        if i >= k_index:
            count += balance_count.get(balance, 0)
            count += balance_count.get(balance - 1, 0)
        
        if i < k_index:
            balance_count[balance] = balance_count.get(balance, 0) + 1

    return count

nums1 = [3, 2, 1, 4, 5]
k1 = 4
print(countSubarraysWithMedianK(nums1, k1)) 

nums2 = [2, 3, 1]
k2 = 3
print(countSubarraysWithMedianK(nums2, k2))  