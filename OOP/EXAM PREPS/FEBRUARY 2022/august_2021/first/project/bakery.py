from typing import List

from project.baked_food.baked_food import BakedFood
from project.drink.drink import Drink
from project.table.table import Table
from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    VALID_FOOD = {
        "Bread": Bread,
        "Cake": Cake
    }
    VALID_DRINK = {
        "Tea": Tea,
        "Water": Water
    }

    VALID_TABLE = {
        "InsideTable": InsideTable,
        "OutsideTable": OutsideTable,
    }

    def __init__(self, name: str):
        self.name = name

        self.food_menu: List[BakedFood] = []
        self.drink_menu: List[Drink] = []
        self.tables_repository: List[Table] = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Name cannot"
                             " be empty string"
                             " or white space!")
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        if food_type in self.VALID_FOOD.keys():
            if name in [x.name for x in self.food_menu if x.name == name]:
                raise Exception(f"{food_type} {name} is already in the menu!")
            cur_food = self.VALID_FOOD[food_type](name, price)
            self.food_menu.append(cur_food)
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: int, brand: str):
        if drink_type in self.VALID_DRINK.keys():
            if name in [x.name for x in self.drink_menu if x.name == name]:
                raise Exception(f"{drink_type} {name} is already in the menu!")
            cur_drink = self.VALID_DRINK[drink_type](name, portion, brand)
            self.drink_menu.append(cur_drink)
        return f"Added {name} ({drink_type}) to the frink menu"

    def add_table(self,table_type: str, table_number: int, capacity: int):
        if table_type not in self.VALID_TABLE:
            return
        if table_number in [t.table_number for t in self.tables_repository if t.table_number == table_number]:
            raise Exception(f"Table {table_number} is already in the bakery!")

        cur_table = self.VALID_TABLE[table_type](table_number,capacity)
        self.tables_repository.append(cur_table)
        return f"Added table number {table_number} in the bakery"

    def reserve_table (self,number_of_people: int):
        available_tables = [t for t in self.tables_repository if t.capacity >= number_of_people]
        if available_tables:
            table = available_tables[0]
            table.reserve(number_of_people)
            return f"Table {table.table_number} has been reserved for {number_of_people} people"
        return f"No available available_tables for {number_of_people} people"

    def order_drink(self, table_number: int, *args):
        cur_table = [t for t in self.tables_repository if t.table_number == table_number]
        if cur_table:
            table = cur_table[0]
            res = [f"Table {table_number} ordered:"]
            for item in args:
                if item in [i.name for i in self.drink_menu]:
                    drink = next(drink for drink in self.drink_menu if drink.name == item)
                    table.drink_orders.append(drink)
                    res.append(f"- {drink.name} {drink.brand} - {drink.portion}ml - {drink.price:.2f}lv")
            res.append(f"{self.name} does not have in the menu:")
            for item in args:
                if item not in [i.name for i in self.drink_menu]:
                    res.append(f"{item}")
            return '\n'.join(res)
        return f"Could not find table {table_number}"

    def order_food(self, table_number: int, *args):
        cur_table = [t for t in self.tables_repository if t.table_number == table_number]
        if cur_table:
            table = cur_table[0]
            res = [f"Table {table_number} ordered:"]
            for item in args:
                if item in [i.name for i in self.food_menu]:
                    food = next(food for food in self.food_menu if food.name == item)
                    table.food_orders.append(food)
                    res.append(f"- {food.name}: {food.portion:.2f}g - {food.price:.2f} lv")
            res.append(f"{self.name} does not have in the menu:")
            for item in args:
                if item not in [i.name for i in self.food_menu]:
                    res.append(f"{item}")
            return '\n'.join(res)
        return f"Could not find table {table_number}"

    def leave_table (self,table_number: int):
        cur_table = [t for t in self.tables_repository if t.table_number == table_number]
        bill = cur_table[0].get_bill()
        self.total_income += bill

        cur_table[0].clear()
        return (f"Table: {table_number}\n"
                f"Bill: {bill:.2f}")
    def get_free_tables_info(self):
        result = ''
        for table in self.tables_repository:
            if not table.is_reserved:
                result += table.free_table_info() + '\n'
        return result.strip()

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"


