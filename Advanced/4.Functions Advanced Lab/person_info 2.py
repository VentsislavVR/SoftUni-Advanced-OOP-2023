def get_info(**param):
    return f"This is {param['name']} from {param['town']} and he is {param['age']} years old"
def get_info2(name,age,town):
    return f"This is {name} from {town} and he is {age} years old"


print(get_info(**{"name": "George",
                  "town":"Sofia",
                  "age": 20}))

print(get_info2(**{"name": "Venci",
                   "town":"Tx",
                   "age": 29}))