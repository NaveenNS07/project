from math import gcd

def minNumberSubarrays(nums):
    def check_valid(arr):
        return gcd(arr[0], arr[-1]) > 1

    if not check_valid(nums):
        return -1

    count = 1
    for i in range(1, len(nums)):
        if not check_valid(nums[:i+1]):
            count += 1

    return count

nums = [2, 6, 3, 4, 3]
print(minNumberSubarrays(nums))  