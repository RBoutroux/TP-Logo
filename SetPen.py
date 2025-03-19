from instruction import Instruction
from Parametre import Parametre

class SetPen(Instruction):
    def __init__(self, turtle, pen):
        super().__init__(turtle)
        self.pen = pen

    def code(self):
        self.turtle.set_pen(self.pen)

    def replace_parametre(self, dict):
        if isinstance(self.pen, Parametre) and self.pen.nom in dict:
            self.pen = self.pen.instantiate(dict)

    def __str__(self):
        return f"SetPen({self.pen})"