from typing import List

from project.client import Client
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.meal import Meal
from project.meals.starter import Starter


class FoodOrdersApp:
    VALID_MEAL_TYPES = {
        "Starter": Starter,
        "MainDish": MainDish,
        "Dessert": Dessert, }
    receipt_id = 0

    def __init__(self):
        self.menu: List[Meal] = []
        self.clients_list: List[Client] = []

    def register_client(self, client_phone_number: str):
        if client_phone_number in [c.phone_number for c in self.clients_list]:
            raise Exception("The client has already been registered!")
        new = Client(client_phone_number)
        self.clients_list.append(new)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if meal.__class__.__name__ in self.VALID_MEAL_TYPES:
                self.menu.append(meal)

    def show_menu(self):
        self.__check_menu()
        meals_in_menu = [m.details() for m in self.menu]
        return '\n'.join(meals_in_menu)

    def __check_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        self.__check_menu()
        if client_phone_number in [c.phone_number for c in self.clients_list]:
            if not client_phone_number:
                self.register_client(client_phone_number)

        cur_client = [c for c in self.clients_list if c.phone_number == client_phone_number][0]
        cur_shopping_cart = []
        cur_bill = 0

        for meal_name,meal_quantity in meal_names_and_quantities.items():
            for meal in self.menu:
                if meal.name == meal_name:
                    if meal.quantity >= meal_quantity:
                        cur_shopping_cart.append(meal)
                        cur_bill += meal.price * meal_quantity
                        meal.quantity -= meal_quantity
                        break

                    else:
                        raise Exception(f"Not enough quantity of {type(meal).__name__}: {meal_name}!")
            else:
                raise Exception(f"{meal_name} is not on the menu!")

        cur_client.shopping_cart.extend(cur_shopping_cart)
        cur_client.bill += cur_bill
        return f"Client {client_phone_number} successfully ordered {', '.join(x.name for x in cur_client.shopping_cart)} for {cur_client.bill:.2f}lv."
    def cancel_order(self, client_phone_number: str):
        cur_client = [c for c in self.clients_list if c.phone_number == client_phone_number][0]
        if len(cur_client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")
        for meal in self.menu:
            meal.quantity += cur_client.shopping_cart[meal.quantity]
        cur_client.bill = 0
        cur_client.shopping_cart.clear()
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        cur_client = [c for c in self.clients_list if c.phone_number == client_phone_number][0]
        if len(cur_client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")
        FoodOrdersApp.receipt_id += 1
        return f"Receipt #{self.receipt_id} with total amount of {cur_client.bill:.2f} was successfully paid for {client_phone_number}."



    def __str__(self):
        return (f"Food Orders App has {len(self.menu)}"
                f" meals on the menu and {len(self.clients_list)} clients.")


food_orders_app = FoodOrdersApp()
print(food_orders_app.register_client("0899999999"))
french_toast = Starter("French toast", 6.50, 5)
hummus_and_avocado_sandwich = Starter("Hummus and Avocado Sandwich", 7.90)
tortilla_with_beef_and_pork = MainDish("Tortilla with Beef and Pork", 12.50, 12)
risotto_with_wild_mushrooms = MainDish("Risotto with Wild Mushrooms", 15)
chocolate_cake_with_mascarpone = Dessert("Chocolate Cake with Mascarpone", 4.60, 17)
chocolate_and_violets = Dessert("Chocolate and Violets", 5.20)
print(food_orders_app.add_meals_to_menu(
    french_toast, hummus_and_avocado_sandwich,
    tortilla_with_beef_and_pork,
    risotto_with_wild_mushrooms,
    chocolate_cake_with_mascarpone,
    chocolate_and_violets))
print(food_orders_app.show_menu())
food = {"Hummus and Avocado Sandwich": 5,
        "Risotto with Wild Mushrooms": 1,
        "Chocolate and Violets": 4}
print(food_orders_app.add_meals_to_shopping_cart('0899999999', **food))
additional_food = {"Risotto with Wild Mushrooms": 2,
                   "Tortilla with Beef and Pork": 2}
print(food_orders_app.add_meals_to_shopping_cart('0899999999', **additional_food))
print(food_orders_app.finish_order("0899999999"))
print(food_orders_app)
