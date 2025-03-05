from abc import ABC, abstractmethod

class Instruction:
    def __init__(self, turtle):
        self.turtle = turtle

    @abstractmethod
    def code(self):
        pass