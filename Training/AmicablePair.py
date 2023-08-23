'''

Amicable Pair

'''

a,b=map(int,input().split())
s1=0
s2=0
for i in range(1,a):
    if(a%i==0):
        s1+=i 
for i in range(1,b):
    if(b%i==0):
        s2+=i 
if(a==s2 and b==s1):
    print("Amicable Pair")
else:
    print("Not Amicable Pair")

