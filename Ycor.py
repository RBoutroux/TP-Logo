from Negated import Negated
class Ycor(Negated):
    def __init__(self):
        super().__init__()
        self.y = 0
    
    def value(self, turtle):
        y = turtle.y
        return self.sign*y