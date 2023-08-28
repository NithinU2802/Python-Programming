'''

    Format Usage and implementation

'''

n=int(input())
m=n/2
print(format(n,".2f"))
print("{0} {1}".format(m,n))
print("{1}".format(m,n))

print("{2}".format(m,n,15))
print("{0} {2} {1}".format(m,n,15,8.5))
