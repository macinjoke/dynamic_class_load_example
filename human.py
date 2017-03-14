from abc import ABCMeta, abstractmethod


class Human(metaclass=ABCMeta):

    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    @abstractmethod
    def execute(self):
        return
