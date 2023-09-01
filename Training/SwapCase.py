'''

    SwapCase character of the string

'''

s=""
a=input()
for j in range(len(a)):
    i=a[j]
    if(i>='a' and i<='z'):
        s+=i.upper()
    elif(i>='A' and i<='Z'):
        s+=i.lower()
    else:
        s+=i 
print(s)

