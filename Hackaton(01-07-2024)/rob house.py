def rob(nums):
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]

    def linear(nums):
        prev = 0
        curr = 0
        for num in nums:
            temp = curr
            curr = max(prev + num, curr)
            prev = temp
        return curr

    rob1 = linear(nums[:-1])
    rob2 = linear(nums[1:])

    return max(rob1, rob2)

houses = [2, 3, 2]
print(rob(houses)) 
