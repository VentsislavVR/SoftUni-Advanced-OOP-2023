from typing import List

from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    VALID_DIVERS = {
        "FreeDiver": FreeDiver,
        "ScubaDiver": ScubaDiver,
    }
    VALID_FISH = {
        "PredatoryFish": PredatoryFish,
        "DeepSeaFish": DeepSeaFish,
    }

    def __init__(self):
        self.divers: List[BaseDiver] = []
        self.fish_list: List[BaseFish] = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in self.VALID_DIVERS:
            return f"{diver_type} is not allowed in our competition."
        if any(existing_diver.name == diver_name for existing_diver in self.divers):
            return f"{diver_name} is already a participant."
        diver = self.VALID_DIVERS[diver_type](diver_name)
        self.divers.append(diver)
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.VALID_FISH:
            return f"{fish_type} is forbidden for chasing in our competition."
        if any(existing_fish.name == fish_name for existing_fish in self.fish_list):
            return f"{fish_name} is already permitted."
        fish = self.VALID_FISH[fish_type](fish_name, points)
        self.fish_list.append(fish)
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        diver = [x for x in self.divers if x.name == diver_name]
        if not diver:
            return f"{diver_name} is not registered for the competition."

        fish = [x for x in self.fish_list if x.name == fish_name]
        if not fish:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver[0].has_health_issue == True:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver[0].oxygen_level < fish[0].time_to_catch:
            diver[0].miss(fish[0].time_to_catch)
            return f"{diver_name} missed a good {fish_name}."
        elif diver[0].oxygen_level == fish[0].time_to_catch:
            if is_lucky:
                diver[0].hit(fish[0])
                return f"{diver_name} hits a {fish[0].points}pt. {fish_name}."
            else:
                diver[0].miss(fish[0].time_to_catch)
                return f"{diver_name} missed a good {fish_name}."
        else:
            diver[0].hit(fish[0])
            return f"{diver_name} hits a {fish[0].points}pt. {fish_name}."

    def health_recovery(self):
        count = 0
        for diver in self.divers:
            if diver.has_health_issue:
                diver.update_health_status()
                diver.renew_oxy()
                count += 1
        return f"Divers recovered: {count}"

    # def diver_catch_report(self, diver_name: str):
    #     diver = next((x for x in self.divers if x.name == diver_name), None)
    #
    #     res = [f"**{diver_name} Catch Report**"]
    #     for fish in diver.catch:
    #         res.append(f"{fish.fish_details()}")
    #
    #     return '\n'.join(x for x in res).strip()
    def diver_catch_report(self, diver_name: str):
        diver = next((x for x in self.divers if x.name == diver_name), None)


        report_lines = [f"**{diver_name} Catch Report**"]
        report_lines.extend(fish.fish_details() for fish in diver.catch)

        return '\n'.join(report_lines).strip()

    def competition_statistics(self):
        healthy_divers = [diver for diver in self.divers if not diver.has_health_issue]

        sorted_divers = sorted(healthy_divers, key=lambda x: (-x.competition_points, -len(x.catch), x.name))

        result = "**Nautical Catch Challenge Statistics**\n"
        result += '\n'.join(str(diver) for diver in sorted_divers)

        return result


