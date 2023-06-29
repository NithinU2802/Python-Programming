'''

  Inheritance in python
  
  Student consist of persons which represented below

'''

class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    
    def print(self):
        print(fname,lname)

class Student(Person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.grad=year
    
    def welcome(self):
        print("Hello",self.fname,self.fname,"you are graduated at ",self.grad)


fun=Student("Nithin","U",2024)
fun.welcome()
