'''

   Lambda function usage in python
   (Powerfull and anonymous function)

'''

def function(n):
    return lambda a:a*n 

fun=function(8)
print(fun(8))

myfun=lambda a,b,c: a*b*c 
print(myfun(2,3,4))
