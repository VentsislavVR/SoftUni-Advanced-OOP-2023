from typing import List

from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.musician import Musician
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIANS = (
        "Guitarist",
        "Drummer",
        "Singer",
    )

    def __init__(self):
        self.band: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.VALID_MUSICIANS:
            raise ValueError("Invalid musician type!")

        cur_musician = [m for m in self.musicians if m.name == name]
        if name in cur_musician:
            raise ValueError(f"{name} is already a musician!")

        self.musicians.append(Musician(name, age))
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        pass

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        pass


    def add_musician_to_band(self, musician_name: str, band_name: str):
        pass


    def remove_musician_from_band(self, musician_name: str, band_name: str):

        pass

    def start_concert(self,concert_place: str, band_name: str):
        pass