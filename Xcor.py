from Negated import Negated
class Xcor(Negated):
    def __init__(self):
        super().__init__()
        self.x = 0
    
    def value(self, turtle):
        x = turtle.x
        return self.sign*x