nums = [3, 6, 2, 7, 1]
k = 6

count = 0 
for i in range(len(nums)): 
   product = 1 
   for j in range(i, len(nums)):
       product *= nums[j] 
       if product % k == 0:
          count += 1

print(count)