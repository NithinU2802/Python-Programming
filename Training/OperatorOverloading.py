'''

    Operator Overloading

'''

class A():
    def  __add__(self,a):
        return self.d+a.d;
    def __init__(self,a):
        self.d=a 
    def value(self):
        return self.d
a=A(8)
b=A(4)
print(a+b)
