from Negated import Negated
class Heading(Negated):
    def __init__(self):
        super().__init__()
        self.direction = 0
    
    def value(self, turtle):
        direction = turtle.angle
        return self.sign*direction