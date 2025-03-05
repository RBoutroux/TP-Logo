from instruction import Instruction

class Forward(Instruction):
    def __init__(self, turtle, distance):
        super().__init__(turtle)
        self.distance = distance
    
    def code(self):
        self.turtle.forward(self.distance)
