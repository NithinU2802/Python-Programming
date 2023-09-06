'''

Input:
4

Ouput:
*  *


*  *

'''

n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 and j==0 or i==0 and j==n-1 or i==n-1 and j==0 or i==n-1 and j==n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
