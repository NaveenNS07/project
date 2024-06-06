def reverse(n):
   if len(n) == 0:
      return n
   else:
      return reverse(n[1:]) + n[0]
result = str(input("Enter the string that needs to be reversed : "))
print("The string is :",result)
print("The reversed string is :",reverse(result))