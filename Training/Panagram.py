'''

Panagram

'''

a="abcdefghijklmnopqrstuvwxyz"
s=input().lower()
f=0
for i in a:
    if i not in s:
        f=1
        break
if f==0 :
    print("Panagram")
else:
    print("Not Panagram")
