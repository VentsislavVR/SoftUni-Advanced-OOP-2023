from typing import List

from project.clients.adult import Adult
from project.clients.base_client import BaseClient
from project.clients.student import Student
from project.loans.base_loan import BaseLoan
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    VALID_LOANS = {
        "StudentLoan": StudentLoan,
        "MortgageLoan": MortgageLoan,
    }
    VALID_CLIENTS = {
        "Student": Student,
        "Adult": Adult,
    }
    LOAN_CHECK = {
        'MortgageLoan': 'Adult',
        'StudentLoan': 'Student',
    }

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: List[BaseLoan] = []
        self.clients: List[BaseClient] = []

    def add_loan(self, loan_type: str) -> str:
        # if loan_type not in self.VALID_LOANS:
        #     raise Exception("Invalid loan type!")
        #
        # self.loans.append(self.VALID_LOANS[loan_type]())
        #
        # return f"{loan_type} was successfully added."
        ...

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        # if client_type not in self.VALID_CLIENTS:
        #     raise Exception("Invalid client type!")
        # if self.capacity == len(self.clients):
        #     return "Not enough bank capacity."
        # self.clients.append(self.VALID_CLIENTS[client_type](client_name, client_id, income))
        #
        # return f"{client_type} was successfully added."
        ...

    def get_loan(self, loan_type):
        # loan = next((x for x in self.loans if x.__class__.__name__ == loan_type), None)
        # return loan
        ...

    def get_client(self, client_id):
        # client = next((x for x in self.clients if x.client_id == client_id), None)
        # return client
        ...

    def grant_loan(self, loan_type: str, client_id: str):
        # loan = self.get_loan(loan_type)
        # client = self.get_client(client_id)
        #
        # if loan and client and loan.__class__.__name__ == self.LOAN_CHECK[loan_type] + 'Loan':
        #     # Remove the loan from the bank's loan collection
        #     granted_loan = self.loans.pop(self.loans.index(loan))
        #
        #     client.loans.append(granted_loan)
        #
        #     return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."
        # else:
        #     raise Exception("Inappropriate loan type!")
        ...
    def remove_client(self,client_id: str):
        ...
    def increase_loan_interest(self,loan_type: str):
        ...
    def increase_clients_interest(self,min_rate: float):
        ...
    def get_statistics(self):
        ...


