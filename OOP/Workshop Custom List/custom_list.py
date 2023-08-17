class CustomList:
    def __init__(self, *args):
        self.__list = [*args]

    def append(self, value):
        self.__list.append(value)
        return self.__list

    def __check_index(self, index):
        if not isinstance(index, int):
            raise ValueError("INDEX MUST BE OF TYPE INT")

        if not (0 <= index <= len(self.__list)) and not (index < 0 and index >= -len(self.__list)):
            raise ValueError("INDEX IS OUT OF RANGE")

    def check_value_in_list(self, value):
        if value not in self.__list:
            raise ValueError("VALUE IS NOT IN THE LIST")
        return self.__list.index(value)

    def remove(self, index):
        self.__check_index(index)
        return self.__list.pop(index)

    def get(self, index):
        self.__check_index(index)
        return self.__list[index]

    def extend(self, values):
        self.__list.extend(values)
        return self.__list

    def insert(self, index, value):
        self.__check_index(index)
        self.__list.insert(index, value)
        return self.__list

    def pop(self):
        if len(self.__list) == 0:
            raise ValueError("LIST IS EMPTY")
        return self.__list.pop(-1)

    def clear(self):
        self.__list = []

    def index(self, value):
        self.check_value_in_list(value)

    def count(self, value):
        return self.count(value)

    def reverse(self):
        return self.__list[::-1]

    def copy(self):
        return self.__list.copy()

    def size(self):
        return len(self.__list)

    def add_first(self, value):
        self.insert(0, value)

    def dictionize(self):
        result = {}
        for idx in range(0, len(self.__list), 2):
            key = self.__list[idx]
            try:
                value = self.__list[idx + 1]
            except IndexError:
                value = ' '
            result[key] = value
        return result

    def move(self, n):
        if isinstance(n, int):
            raise ValueError("N MUST BE INT")
        if n >= len(self.__list):
            raise ValueError("LOL")
        first_part = self.__list[:n]
        second_part = self.__list[n:]
        self.__list = second_part + first_part
        return self.__list

    def sum(self):
        result = 0
        for el in self.__list:
            result += self.__return_el_or_len(el)

        return result
    def __return_el_or_len(self,el):
        try:
            return len(el)
        except TypeError:
            return el

    def overbounds(self):
        result = 0
        max_num = float("-inf")
        biggest_index = None

        for index in range(0,len(self.__list)):
            current = self.__return_el_or_len(self.__list[index])
            if current > max_num:
                max_num=current
                biggest_index = index

        return biggest_index
    def underbound(self):
        min_num = float("inf")
        smallest_index = None

        for index in range(0,len(self.__list)):
            current = self.__return_el_or_len(self.__list[index])
            if current < min_num:
                min_num = current
                smallest_index = index

        return smallest_index