'''

    Usage of ljust Method and lambda

'''


a="String"

print(a.ljust(20))
print(a.ljust(20,'0'))

x = lambda : 10
print(x())

x=lambda a,b: a+b 
print(x(9,10))

# Represents the function
print(type(x))
