'''

Prime digits in a number 

Eg-1: 
123456 ->  2 3 5 

Eg-2:
87546363 -> 7 5 3 3  

'''

n=input()
for i in range(len(n)):
    f=0
    a=int(n[i])
    if(a==1):
        continue
    for j in range(2,a):
        if a%j==0:
            f=1;
            break;
    if f==0:
        print(a,end=" ")

