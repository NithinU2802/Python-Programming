'''

    Exception Handling in python

'''

def Divison(a,b):
    try:
        r=a/b 
        print(r)
    except:
        print("Zero Division Error")

a=int(input())
b=int(input())
Divison(a,b)
