from typing import List

from project.car.car import Car
from project.core.car_factory import CarFactory
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars: List[Car] = []
        self.drivers: List[Driver] = []
        self.races: List[Race] = []

        self.car_factory = CarFactory()

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if any(c.model == model for c in self.cars):
            raise Exception(f"Car {model} is already created!")

        try:
            car = self.car_factory.create_car(
                car_type, model, speed_limit)
            self.cars.append(car)
            return f"{car.__class__.__name__} {car.model} is created."
        except RuntimeError:
            pass

    def create_driver(self, driver_name: str):
        if any(d.name == driver_name for d in self.drivers):
            raise Exception(f"Driver {driver_name} is already created!")
        driver = Driver(driver_name)
        self.drivers.append(driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if any(r.name == race_name for r in self.races):
            raise Exception(f"Race {race_name} is already created!")
        race = Race(race_name)
        self.races.append(race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self.__find_driver_by_name(driver_name)

        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")

        car = self.__find_last_free_car_by_type(car_type)

        if car is None:
            raise Exception(f"Car {car_type} could not be found!")

        return driver.change_car(car)

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = self.__find_race_by_name(race_name)
        if race is None:
            raise Exception(f"Race {race_name} could not be found!")

        driver = self.__find_driver_by_name(driver_name)
        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")

        return race.register_driver(driver)

    def start_race(self, race_name: str):
        race = self.__find_race_by_name(race_name)
        if race is None:
            raise Exception(f"Race {race_name} could not be found!")
        race.start()

    def __find_driver_by_name(self, driver_name):
        for d in self.drivers:
            if d.name == driver_name:
                return d
        return None

    def __find_last_free_car_by_type(self, car_type):
        for idx in range(len(self.cars) - 1, -1, -1):
            car = self.cars[idx]

            if not car.is_taken and car.__class__.__name__ == car_type:
                return car
        return None

    def __find_race_by_name(self, race_name):
        for r in self.races:
            if r.name == race_name:
                return r
        return None
