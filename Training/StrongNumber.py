'''

Strong Number

'''

n=int(input())
t=n
res=0
while(t>0):
    s=1
    for i in range(2,(t%10)+1):
        s*=i
    res+=s 
    t//=10
if res==n:
    print("Strong Number")
else:
    print("Not Strong Number")
