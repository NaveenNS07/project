def maxmin(arr):
    minimum = min(arr)
    maximum = max(arr)
    return minimum, maximum

arr = [11,13,15,17,19,21,23,35,37]

minimum, maximum = maxmin(arr)
print("Min=",minimum,"Max=",maximum)
