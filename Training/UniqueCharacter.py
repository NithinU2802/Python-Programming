'''

Unique Character of two string and print in ascending order

'''

a=input()
b=input()
s=set()
for i in a:
    if i not in b:
        s.add(i)
        
for i in b:
    if i not in a:
        s.add(i)
s=list(s)
s=sorted(s)
print(s)
