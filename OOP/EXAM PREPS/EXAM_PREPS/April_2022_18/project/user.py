from typing import List


class User:
    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked: List = []
        self.movies_owned: List = []

    @property
    def username(self):
        return self.__name

    @username.setter
    def username(self, value):
        if value == '':
            raise ValueError('Invalid username!')
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 6:
            raise ValueError('Users under the age of 6 are not allowed!')
        self.__age = value

    def __str__(self):
        result = f"Username: {self.username}, Age: {self.age}\n"

        result += f"Liked movies:\n"
        if not self.movies_liked:
            result += f"No movies liked.\n"
        else:
            pass
            result += '\n'.join(lm.details for lm in self.movies_liked)

        result += "Owned movies:\n"

        if not self.movies_owned:
            result += f"No movies owned.\n"
        else:

            result += '\n'.join(om.details for om in self.movies_owned)

        return result
