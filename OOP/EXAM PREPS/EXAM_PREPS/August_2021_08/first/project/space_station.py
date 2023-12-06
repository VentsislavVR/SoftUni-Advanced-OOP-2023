from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    VALID_ASTRONAUTS = {
        "Biologist": Biologist,
        "Geodesist": Geodesist,
        "Meteorologist": Meteorologist,
    }

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.successful_mission = 0
        self.failed_mission = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."

        astronaut = self.__create_astronaut(astronaut_type, name)

        self.astronaut_repository.add(astronaut)
        return f"Successfully added {astronaut_type}: {astronaut.name}."

    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."

        planet = Planet(name)
        planet.items = items.split(', ')

        self.planet_repository.add(planet)

        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astro = self.astronaut_repository.find_by_name(name)
        if astro is None:
            raise Exception(f"Astronaut {name} doesn't exist!")

        self.astronaut_repository.remove(astro)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        [a.increase_oxygen(10) for a in self.astronaut_repository.astronauts]

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)
        if planet is None:
            raise Exception("Invalid planet name!")

        astronauts = self.astronaut_repository.find_astronauts_for_mission(5, 30)

        if len(astronauts) == 0:
            raise Exception("You need at least one astronaut to explore the planet!")

        participants = 0
        for astro in astronauts:
            if len(planet.items) == 0:
                break
            while astro.oxygen > 0 and len(planet.items) > 0:
                astro.backpack.append(planet.items.pop())
                astro.breathe()
            participants += 1

        if len(planet.items) == 0:
            self.successful_mission += 1
            return f"Planet: {planet_name} was explored. {participants} astronauts participated in collecting items."
        else:
            self.failed_mission += 1
            return f"Mission is not completed."

    def report(self):
        result = f"{self.successful_mission} successful missions!" + '\n'
        result += f"{self.failed_mission} missions were not completed!" + '\n'
        result += "Astronauts' info:" + '\n'
        for astro in self.astronaut_repository.astronauts:
            result += str(astro) + '\n'

        return result.strip()

    @staticmethod
    def __create_astronaut(astronaut_type, name):
        if astronaut_type in SpaceStation.VALID_ASTRONAUTS:
            return SpaceStation.VALID_ASTRONAUTS[astronaut_type](name)
        raise Exception("Astronaut type is not valid!")
