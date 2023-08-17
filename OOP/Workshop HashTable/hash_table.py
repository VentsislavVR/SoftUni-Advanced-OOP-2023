class HashTable:
    def __init__(self):
        self.__max_capacity = 4
        self.__keys = [None] * self.__max_capacity  # [None, None, None,None]
        self.__values = [None] * self.__max_capacity  # [None, None, None,None]
        self.__length = 0

    def add(self,key,value):
        self[key] = value

    def remove(self,key):
        self.__delitem__(key)

    def get(self,key,message=None):
        try:
            return self[key]
        except KeyError:
            return message

    def __getitem__(self, key):
        try :
            index = self.__keys.index(key)
            return self.__values[index]
        except ValueError:
            raise KeyError(f"{key} is not in the hash table")
    def __delitem__(self, key):
        try :
            index = self.__keys.index(key)
            self.__keys[index] = None
            self.__values[index] = None
            self.__length -= 1
        except ValueError:
            raise KeyError(f"{key} is not in the hash table")




    def __setitem__(self, key, value):
        try:
            index = self.__keys.index(key)
            self.__values[index] = value
        except ValueError:
            pass
        else:
            return

        if len(self) == self.__max_capacity:
            self.__resize()

        index = self.__calc_index(key)
        self.__keys[index] = key
        self.__values[index] = value

        self.__length += 1

    def __resize(self):
        self.__keys = self.__keys + [None] * self.__max_capacity
        self.__values = self.__values + [None] * self.__max_capacity

        self.__max_capacity *= 2

    def __calc_index(self, key):
        index = sum(ord(c) for c in str(key)) % self.__max_capacity
        index = self.__get_index(index)

        return index

    def __get_index(self, index):
        while True:
            if self.__keys[index % self.__max_capacity] is None:
                return index % self.__max_capacity
            index += 1

    def __len__(self):
        return self.__length

    def __str__(self):
        result = []

        for i in range(self.__max_capacity):
            if self.__keys[i] is not None:
                result.append(f"{self.__keys[i]}: {self.__values[i]}")
        return "{" + ', '.join(result) + "}"


table = HashTable()
table["name"] = "Peter"
table["age"] = 25
table["is_pet_owner"] = True
table["is_driver"] = False
table["can_fight"] = True
table.remove("can_fight")
print(table.get("name"))
print(table)
# print(table.get("name"))
# print(table["age"])
# print(len(table))
