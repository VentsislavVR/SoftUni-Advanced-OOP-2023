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
    GRANTED_LOANS = [0,0]

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: List[BaseLoan] = []
        self.clients: List[BaseClient] = []


    def add_loan(self, loan_type: str) -> str:
        if loan_type not in self.VALID_LOANS:
            raise Exception("Invalid loan type!")

        self.loans.append(self.VALID_LOANS[loan_type]())

        return f"{loan_type} was successfully added."


    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.VALID_CLIENTS:
            raise Exception("Invalid client type!")
        if self.capacity == len(self.clients):
            return "Not enough bank capacity."
        self.clients.append(self.VALID_CLIENTS[client_type](client_name, client_id, income))

        return f"{client_type} was successfully added."


    def get_loan(self, loan_type):
        loan = next((x for x in self.loans if x.__class__.__name__ == loan_type), None)
        return loan
        # first loan ...


    def get_client(self, client_id):
        client = next((x for x in self.clients if x.client_id == client_id), None)
        return client


    def grant_loan(self, loan_type: str, client_id: str):
        loan = self.get_loan(loan_type)
        client = self.get_client(client_id)
        can_grant = False
        if ((loan.__class__.__name__ == 'StudentLoan' and client.__class__.__name__ == 'Student')
                or
                loan.__class__.__name__ == 'MortgageLoan' and client.__class__.__name__ == 'Adult') :

            can_grant = True
        if can_grant == True :

            client.loans.append(loan)
            self.loans.remove(loan)
            self.GRANTED_LOANS[0] +=1
            self.GRANTED_LOANS[1] += loan.amount

            return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."
        else:
            raise Exception("Inappropriate loan type!")

    def remove_client(self,client_id: str):
        client = self.get_client(client_id)
        if client is None:
            raise Exception("No such client!")
        if len(client.loans) > 0:
            raise Exception("The client has loans! Removal is impossible!")
        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self,loan_type: str):
        counter = 0
        for l in self.loans:
            if l.__class__.__name__ == loan_type:
                l.increase_interest_rate()
                counter += 1
        return f"Successfully changed {counter} loans."

    def increase_clients_interest(self,min_rate: float):
        counter = 0
        for c in self.clients:
            if c.interest < min_rate:
                c.increase_clients_interest()
                counter += 1
        return f"Number of clients affected: {counter}."
    def get_statistics(self):
        total_clients_income = sum([x.income for x in self.clients])
        avg = sum(x.interest for x in self.clients) / len(self.clients) if len(self.clients) > 0 else 0

        return (f"Active Clients: {len(self.clients)}\n"
                f"Total Income: {total_clients_income:.2f}\n"
                f"Granted Loans: {self.GRANTED_LOANS[0]}, Total Sum: {self.GRANTED_LOANS[1]:.2f}\n"
                f"Available Loans: {len(self.loans)}, Total Sum: {sum(x.amount for x in self.loans):.2f}\n"
                f"Average Client Interest Rate: {avg:.2f}")



# bank = BankApp(3)
#
# print(bank.add_loan('StudentLoan'))
# print(bank.add_loan('MortgageLoan'))
# print(bank.add_loan('StudentLoan'))
# print(bank.add_loan('MortgageLoan'))
#
#
# print(bank.add_client('Student', 'Peter Simmons', '1234567891', 500))
# print(bank.add_client('Adult', 'Samantha Peters', '1234567000', 1000))
# print(bank.add_client('Student', 'Simon Mann', '1234567999', 700))
# print(bank.add_client('Student', 'Tammy Smith', '1234567555', 700))
#
# print(bank.grant_loan('StudentLoan', '1234567891'))
# print(bank.grant_loan('MortgageLoan', '1234567000'))
# print(bank.grant_loan('MortgageLoan', '1234567000'))
#
# print(bank.remove_client('1234567999'))
#
# print(bank.increase_loan_interest('StudentLoan'))
# print(bank.increase_loan_interest('MortgageLoan'))
#
# print(bank.increase_clients_interest(1.2))
# print(bank.increase_clients_interest(3.5))
#
# print(bank.get_statistics())

