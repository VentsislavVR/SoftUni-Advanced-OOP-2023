from abc import ABC, abstractmethod
from typing import List



class Animal(ABC):

    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @property
    @abstractmethod
    def food_that_eats(self) -> List[object]:
        ...

    @property
    @abstractmethod
    def gained_weight(self) -> float:
        ...

    @abstractmethod
    def make_sound(self) -> str:
        ...

    def feed(self, food) -> None or str:
        if type(food) not in self.food_that_eats:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * self.gained_weight
        self.food_eaten += food.quantity


class Bird(Animal, ABC):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return (f"{self.__class__.__name__} "
                f"[{self.name}, "
                f"{self.wing_size}, "
                f"{self.weight}, "
                f"{self.food_eaten}]")


class Mammal(Animal, ABC):
    def __init__(self, name: str, weight: float, living_region: float):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return (f"{self.__class__.__name__} "
                f"[{self.name},"
                f" {self.weight},"
                f" {self.living_region},"
                f"{self.food_eaten}]")
