from instruction import Instruction

class SetPen(Instruction):
    def __init__(self, turtle, pen):
        super().__init__(turtle)
        self.pen = pen

    def code(self):
        self.turtle.set_pen(self.pen)