from Parametre import Parametre
class Procedure:
    def __init__(self, name):
        self.name = name
        self.parametres = []

    def __init__(self, name, parametres, instructions):
        self.name = name
        self.parametres = parametres
        self.instructions = instructions

    def addParametre(self, parametre):
        if type(parametre) is Parametre:
            self.parametres.append(parametre)
        elif type(parametre) == list(Parametre):
            self.parametres.extend(parametre)
        else:
            raise TypeError("Parametre must be of type Parametre or list(Parametre)")