from copy import deepcopy
class Negated:
    def __init__(self):
        self.sign = 1
    
    def __neg__(self):
        self.sign = -1
        return self
    
    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for attr, value in self.__dict__.items():
            if attr == "turtle":
                setattr(result, attr, value)
            else:
                setattr(result, attr, deepcopy(value, memo))
        return result