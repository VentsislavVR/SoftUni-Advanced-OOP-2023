class FoodFactory:
    VALID_FOOD = {
        "Bread": Bread,
        "Cake": Cake
    }

    def creat_food(self, food_type: str, name: str, price: float):
        return self.__class__.VALID_FOOD[food_type](name, price)
