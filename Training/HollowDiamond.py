'''

    Hollow Diamond

Input: 4

Output:
   1 
  2  2
 3    3
4      4
 3    3 
  2 2
   1

'''

n=int(input())

for i in range(1,n+1):
    for j in range(1,n+n+1):
        if(j==n-i+1 or j==n+i-1):
            print(i,end="")
        else:
            print(end=" ")
    print()
for i in range(n-1,0,-1):
    for j in range(1,n+n+1):
        if(j==n-i+1 or j==n+i-1):
            print(i,end="")
        else:
            print(end=" ")
    print()
