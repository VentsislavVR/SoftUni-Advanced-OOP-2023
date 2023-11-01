from typing import Dict




class Player:
    DEFAULT_GUILD = 'Unaffiliated'
    def __init__(self, name:str, hp:int,mp:int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills:Dict[str:int] = {}
        self.guild:str = Player.DEFAULT_GUILD

    def add_skill(self,skill_name,mana_cost)->str:
        if skill_name not in self.skills:
            self.skills[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.name}"
        return "Skill already added"

    def player_info(self):
        skills_info = "\n".join(f"==={skill_name} - {skill_level}" for skill_name, skill_level in self.skills.items())
        return f'Name: {self.name}\nGuild: {self.guild}\nHP: {self.hp}\nMP: {self.mp}\n{skills_info}\n'





