from collections import Counter

def intersect(nums1, nums2):
    count1, count2 = Counter(nums1), Counter(nums2)
    intersection = []
    
    for num in count1.keys() & count2.keys():
        intersection.extend([num] * min(count1[num], count2[num]))
    
    return intersection