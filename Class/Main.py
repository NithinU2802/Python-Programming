'''

   Learning class and it's functionality 

'''

class Main:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def print(self):
        print(self.fname,self.lname)
    def demo(self):
        print("Hello World")

cls=Main("Nithin","U")
cls.print()
cls.demo()
    
