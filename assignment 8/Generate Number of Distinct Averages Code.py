def numOfDistinctAverages(nums):
    nums.sort()
    distinct_averages = set()
    n = len(nums)
    
    for i in range(n):
        for j in range(i+1, n):
            distinct_averages.add((nums[i] + nums[j]) / 2)
    
    return len(distinct_averages)

nums = [4, 1, 4, 0, 3, 5]
print(numOfDistinctAverages(nums))  