from instruction import Instruction

class PenColor(Instruction):
    def __init__(self, turtle, color):
        super().__init__(turtle)
        self.color = color

    def code(self):
        self.turtle.set_color(self.color)