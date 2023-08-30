from project.drink.drink import Drink


class Tea(Drink):
    def __init__(self, name: str, portion: int, brand: str):
        super().__init__(name, portion, 2.50, brand)

    def __repr__(self):
        return (f"- {self.name} "
                f"{self.brand} - "
                f"{self.portion:.2f}ml -"
                f" {self.price:.2f}lv")
