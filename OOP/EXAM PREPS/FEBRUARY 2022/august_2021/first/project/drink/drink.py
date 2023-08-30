from abc import ABC, abstractmethod


class Drink(ABC):
    def __init__(self, name: str, portion: int, price: float, brand: str):
        self.brand = brand
        self.price = price
        self.portion = portion
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Name cannot be empty string or white space!")
        self.name = value

    @property
    def portion(self):
        return self.__portion

    @portion.setter
    def portion(self, value):
        if value <= 0:
            raise ValueError("Portion cannot be less than or equal to zero!")
        self.portion = value

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        if value.strip() == '':
            raise ValueError("Brand cannot be empty string or white space!")
        self.brand = value

    @abstractmethod
    def __repr__(self):
        return f"- {self.name} {self.brand} - {self.portion:.2f}ml - {self.price:.2f}lv"
