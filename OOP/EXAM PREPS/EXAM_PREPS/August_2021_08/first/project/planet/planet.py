from typing import List

from project.common.validators import Validator


class Planet:
    def __init__(self, name: str):
        self.name = name
        self.items: List = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_str_is_empty(value,"Planet name cannot be empty string or whitespace!")
        self.__name = value
