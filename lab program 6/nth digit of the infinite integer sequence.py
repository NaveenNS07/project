def findNthDigit(n): 
   length, size, start = 1, 9, 1 
   while n > length * size:
     n -= length * size 
     length += 1 
     size *= 10
     start *= 10 
     start += (n - 1) // length 
     return int(str(start)[(n - 1) % length])