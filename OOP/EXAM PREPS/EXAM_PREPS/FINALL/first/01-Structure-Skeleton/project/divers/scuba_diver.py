from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    max_oxygen = 540
    def __init__(self, name: str):
        super().__init__(name, oxygen_level=self.max_oxygen)

    def miss(self, time_to_catch: int):
        oxygen_reduction = int(0.3 * time_to_catch)
        self.oxygen_level = max(0, self.oxygen_level - oxygen_reduction)
        if self.oxygen_level == 0:
            self.has_health_issue = True

    def renew_oxy(self):
        self.oxygen_level = self.max_oxygen