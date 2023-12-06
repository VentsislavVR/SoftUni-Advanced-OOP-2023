from abc import ABC, abstractmethod
from typing import List

from project.common.validators import Validator


class Astronaut(ABC):
    @abstractmethod
    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack: List = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_str_is_empty(value,"Astronaut name cannot be empty string or whitespace!")
        self.__name = value

    def breathe(self):
        self.oxygen -= 10

    def increase_oxygen(self, amount: int):
        self.oxygen += amount

    def __repr__(self):
        return f"{self.name}--{self.oxygen}"

    def __str__(self):
        result =f"Name: {self.name}" + '\n'
        result +=f"Oxygen: {self.oxygen}" + '\n'
        result +=f"Backpack items: {', '.join(x for x in self.backpack) if len(self.backpack) > 0 else 'none'}"

        return result