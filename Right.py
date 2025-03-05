from instruction import Instruction

class Right(Instruction):
    def __init__(self, turtle, angle):
        super().__init__(turtle)
        self.angle = angle

    def code(self):
        self.turtle.right(self.angle)