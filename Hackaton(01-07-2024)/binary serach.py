def binarysearch(arr,key):
    low=0
    high=len(arr)-1
    mid=0

    while low<=high:
        mid=(high+low)//2

        if arr[mid] < key:
            low = mid + 1
        elif arr[mid] > key:
            high = mid - 1
        else:
            return mid

    return -1

arr=[10,20,30,40,50,60]
key=50

result=binarysearch(arr,key)+1
if result != -1:
    print("output:",result)
else:
    print("Element is not present in array")
