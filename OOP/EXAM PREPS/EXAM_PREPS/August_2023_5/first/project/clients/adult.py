from project.clients.base_client import BaseClient


class Adult(BaseClient):
    def __init__(self,name: str, client_id: str, income: float):
        super().__init__(name=name, client_id=client_id, income=income,interest=4.0)

    def increase_clients_interest(self):
        self.interest += 2.0