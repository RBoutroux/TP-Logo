from abc import ABC, abstractmethod
from copy import deepcopy

class Instruction:
    def __init__(self, turtle):
        self.turtle = turtle

    @abstractmethod
    def code(self):
        pass

    @abstractmethod
    def replace_parametre(self, turtle):
        pass
    
    @abstractmethod
    def __str__(self):
        pass

    # def __deepcopy__(self, memo):
    #     # Créer une nouvelle instance sans appeler le constructeur
    #     new_instance = self.__class__.__new__(self.__class__)
        
    #     # Copier tous les attributs de l'objet
    #     memo[id(self)] = new_instance
    #     for attr, value in self.__dict__.items():
    #         setattr(new_instance, attr, deepcopy(value, memo))
        
    #     return new_instance

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