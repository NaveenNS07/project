nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

intersection = [num for num in nums1 if num in nums2]
intersection = list(set(intersection))

print(intersection)