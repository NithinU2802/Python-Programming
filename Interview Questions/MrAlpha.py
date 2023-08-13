"""

Output:
Welcome, Mr.Alpha

"""

class AlphaClass:
    def display_alpha(self):
        print('Welcome, Mr.Alpha')
        
class BetaClass (AlphaClass):
    def display_beta(self):
        print('Welcome, Mr.Beta')
    def __init__(self):
        self.display_beta = super().display_alpha
    def display_alpha (self):
        print('Welcome, Mr.Gamma')
        
obj=BetaClass()
obj.display_beta()
