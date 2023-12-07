from typing import List

from project.core.validators import Validator
from project.driver import Driver


class Race:
    def __init__(self, name:str):
        self.name = name
        self.drivers:List[Driver] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_len_is_len_than(
            value,
            1,
            "Name cannot be an empty string!")

        self.__name = value
