'''

Adams Number

'''

a=int(input())
s1=a*a 
b=0
t=a 
while t>0:
    b=(b*10)+t%10;
    t//=10
t=b*b 
s2=0
while t>0:
    s2=s2*10+t%10
    t//=10
if(s1==s2):
    print("Adam Number")
else:
    print("Not Adam Number")
