
"""""""""""""""""""""""""""""""""""""""""""""""""""""


Sum of two prime number is n...

Input: 34

Output: 3 31


Input: 128

Output: 1 127

"""""""""""""""""""""""""""""""""""""""""""""""""""""

def isprime(a):
    if(a<2):
        return False
    for i in range(2,int(a**0.5)+1):
        if(a%i==0):
            return False
    return True

n=int(input())
f=0
for i in range(1,n):
    s=n-i
    if(isprime(i) and isprime(s)):
        print(i,s)
        f=1
        break
if(f==0):
    print("-1")
