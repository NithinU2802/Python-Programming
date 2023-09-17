'''

Classes and Object
    
    Create an class with constructor and get Person data and
display method to print the user details.

'''

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age  
    def display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
person=Person("Nithin",26)
person.display()
