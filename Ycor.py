from Negated import Negated
from copy import deepcopy

class Ycor(Negated):
    def __init__(self):
        super().__init__()
        self.y = 0
    
    def value(self, turtle):
        y = turtle.y
        return self.sign*y
    
    def __str__(self):
        return f"Ycor({self.sign*turtle.y})"