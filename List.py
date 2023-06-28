'''

   Quality of List in python 

'''

a=list(map(int,input().split(" ")))
if(a[0]>a[1]):
    print("1st Element is Greater")
else:
    print("2nd Element is Greater")
    
a.append(3)
print(a)

a.extend([1,3,4])
print(a)

a.pop(4) # by index
print(a)

a.insert(4,3)
print(a)

print(a[1:3])

print(a.count(3))

print(min(a),max(a))

print(a*2)

