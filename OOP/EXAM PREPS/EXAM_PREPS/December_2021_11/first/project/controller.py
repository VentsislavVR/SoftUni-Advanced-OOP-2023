from typing import List

from project.car.car import Car
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars:List[Car] = []
        self.drivers:List[Driver] = []
        self.races:List[Race] = []

    def create_car(self,car_type: str, model: str, speed_limit: int):
        ...
    def create_driver(self,driver_name: str):
        ...

    def create_race(self,race_name: str):
        ...
    def add_car_to_driver(self,driver_name: str, car_type: str):

        ...
    def add_driver_to_race(self,race_name: str, driver_name: str):

        ...

    def start_race(self,race_name: str):
        ...