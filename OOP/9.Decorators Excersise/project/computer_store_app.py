from typing import List

from project.computer_types.computer import Computer
from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    valid = {"Desktop Computer": DesktopComputer,
             "Laptop": Laptop}

    def __init__(self):
        self.warehouse: List[Computer] = []
        self.profits: int = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        try:
            computer = self.valid[type_computer](manufacturer, model)
        except KeyError:
            raise ValueError(f"{type_computer} is not a valid type computer!")

        configuration = computer.configure_computer(processor, ram)
        self.warehouse.append(computer)
        return configuration

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int) -> str:

        for comp in self.warehouse:
            if comp.ram >= wanted_ram and \
                    comp.processor == wanted_processor \
                    and comp.price <= client_budget:
                self.profits += client_budget - comp.price
                self.warehouse.remove(comp)

                return f"{comp} sold for {client_budget}$."

        raise Exception("Sorry, we don't have a computer for you.")


