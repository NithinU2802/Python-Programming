n=5
lower=97
for i in range(1,n+1):
    x=2*i-1
    for j in range(1,x+1):
        if(j==1 or j==x):
            print("*",end=" ")
        else:
            if(j<=x):
                num=lower-32
                print(chr(num),end=" ")
                lower+=1
    print()
m=n-1
upper=num
for i in range(0,n):
    y=2*m+1
    for j in range(1,y+1):
        if(j==1 or j==y):
            print("*",end=" ")
        else:
            if(j<=y):
                num=upper+32
                print(chr(num),end=" ")
                upper-=1 
    m-=1 
    print()
