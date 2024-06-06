def fact(n):
   if n == 1:
       return n
   else:
       return n*fact(n-1)

num = 5

if num < 0:
   print("enter correct number")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", fact(num))