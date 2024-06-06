def myCopy(s1,s2):
    for i in range(len(s1)):
        s2[i]=s1[i]
    return "".join(s2)
 
s1=list("GEEKSFORGEEKS")
s2=[""]*len(s1)
print(myCopy(s1,s2))