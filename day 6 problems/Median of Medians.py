import statistics

def median_of_medians(arr):
    sublists = [arr[x:x+5] for x in range(0, len(arr), 5)]
    medians = [statistics.median(sublist) for sublist in sublists]
    if len(medians) <= 5:
        pivot = statistics.median(medians)
    else:
        pivot = median_of_medians(medians)
    lower = [x for x in arr if x < pivot]
    upper = [x for x in arr if x > pivot]
    return pivot, lower, upper

arr = [3, 6, 8, 10, 1, 2, 5, 4, 7, 9]
pivot, lower, upper = median_of_medians(arr)

print("Pivot:", pivot)
print("Lower values:", lower)
print("Upper values:", upper)