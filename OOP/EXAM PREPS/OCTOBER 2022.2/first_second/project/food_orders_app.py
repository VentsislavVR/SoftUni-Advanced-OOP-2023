from typing import List

from project.client import Client
from project.meals.meal import Meal


class FoodOrdersApp:
    def __int__(self):
        self.menu: List[Meal] = []
        self.clients_list: List[Client] = []


    def register_client(self, client_phone_number: str):
        ...

    def add_meals_to_menu(self,meals: Meal):
        ...

    def show_menu(self):
        ...

    def add_meals_to_shopping_cart(self,client_phone_number: str, ** meal_names_and_quantities):
        ...
