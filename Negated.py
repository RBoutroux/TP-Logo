class Negated:
    def __init__(self):
        self.sign = 1
    
    def __neg__(self):
        self.sign = -1
        return self