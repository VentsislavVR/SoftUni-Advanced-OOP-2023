from abc import ABC, abstractmethod
from typing import List
from project.baked_food.baked_food import BakedFood
from project.drink.drink import Drink


class Table(ABC):
    def __init__(self, table_number: int, capacity: int):
        self.capacity = capacity
        self.table_number = table_number

        self.food_orders: List[BakedFood] = []
        self.drink_orders: List[Drink] = []
        self.number_of_people: int = 0
        self.is_reserved: bool = False

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        if self.__class__.__name__ == 'InsideTable':
            if not (1 <= value <= 50):
                message = "Inside table's number must be between 1 and 50 inclusive!"
                raise ValueError(message)
            self.__table_number = value

        if self.__class__.__name__ == 'OutsideTable':
            if not (51 <= value <= 100):
                message = "Outside table's number must be between 51 and 100 inclusive!"
                raise ValueError(message)
            self.__table_number = value


    @property
    def capacity(self):
        return self.__capacity


    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Capacity has "
                             "to be "
                             "greater than 0!")
        self.__capacity = value


    def reserve(self, number_of_people: int):
        # if number_of_people <= self.capacity and self.is_reserved == False:
            self.is_reserved = True
            self.number_of_people += number_of_people


    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)


    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)


    def get_bill(self):
        food = sum([f.price for f in self.food_orders])
        drink = sum([d.price for d in self.drink_orders])
        total = food + drink
        return total


    def clear(self):
        self.drink_orders = []
        self.food_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    @abstractmethod
    def free_table_info(self):
       ...

    #     return
    # table_type = 'InsideTable' if 0 < self.table_number <= 50 else 'OutsideTable'
    # # table_type = 'InsideTable' if 1 <= self.table_number <= 50 else (
    # #     'OutsideTable' if 51 <= self.table_number <= 100 else None)
