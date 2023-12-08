from project.rooms.room import Room


class AloneOld(Room):
    room_members_count = 1
    room_cost = 10

    def __init__(self, name: str, pension: float):
        super().__init__(name, pension, self.room_members_count)
