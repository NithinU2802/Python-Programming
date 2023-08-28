s=input()
n=len(s)
for i in range(n):
    for j in range(n):
        if( i==0):
            print(s[j],end=" ")
        elif(j==0):
            print(s[i],end=" ")
        elif(j==n-1):
            print(s[n-i-1],end=" ")
        elif(i==n-1):
            print(s[n-j-1],end=" ")
        else:
            print(" ",end=" ")
    print()



