from project.band_members.musician import Musician

VALID_SKILLS = ("sing high pitch notes",
                "sing low pitch notes")


class Singer(Musician):

    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.available_skills_to_learn = VALID_SKILLS


# s = Singer("Test", 18)
#
# s.learn_new_skill("sing high pitch notes")
# s.learn_new_skill("sing high pitch notes")
# print(s.skills)