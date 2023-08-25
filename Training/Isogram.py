'''

    Isogram

'''

a=input()
char=[]
f=0
for i in a:
    if i in char:
        f=1 
    char.append(i)
if f==0:
    print("Isogram")
else:
    print("Not Isogram")
