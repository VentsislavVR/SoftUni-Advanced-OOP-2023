from typing import Optional


class Room:
    def __init__(self, number: int, capacity: int):
        self.number = number
        self.capacity = capacity
        self.guests = 0
        self.is_taken = False

    def take_room(self, people: int) -> Optional[str]:
        if not self.is_taken and self.capacity >= people:
            self.is_taken = True
            self.guests = people
            return
        return f"Room number {self.number} cannot be taken"

    def free_room(self) -> Optional[str]:
        if not self.is_taken:
            return f"Room number {self.number} is not taken"

        self.is_taken = False
        self.guests = 0
