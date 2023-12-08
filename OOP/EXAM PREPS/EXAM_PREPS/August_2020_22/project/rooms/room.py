from typing import List

from project.people.child import Child


class Room:
    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children: List[Child] = []
        self.expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        self.__validate_expenses(value)
        self.__expenses = value

    def calculate_expenses(self, *args):
        result = 0
        for items in args:
            result += sum(
                x.get_monthly_expense() for x in items
            )
        # self.expenses = sum([sum(el.get_monthly_expense() for el in ll) for ll in args])
        # self.expenses = sum(el.get_monthly_expense() for seq in args for el in seq)
        self.expenses = result

    @staticmethod
    def __validate_expenses(value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")

