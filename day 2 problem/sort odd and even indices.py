def sort_array(nums):
    nums.sort(key=lambda x: (x % 2, x % 2 == 0))
    return nums