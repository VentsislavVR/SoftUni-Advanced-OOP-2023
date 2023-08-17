def Create(direction, value):
    ...


def Update(direction, value):
    ...


def Delete(direction):
    ...


def Read(direction):
    ...

def check_valid_position(row,col):
    ...


SIZE = 6

matrix = [[x for x in input().split()] for x in range(SIZE)]

starting_positions = tuple(input())

directions = {
    "up": (-1,0),
    "down": (1,0),
    "left": (0,-1),
    "right": (0,1),
}

while True:
    command = input()
    if command == "Stop":
        break
                    # i dont get 3 values everytime
    action,direction,value = command.split()

    if action == "Create":
        Create(direction,value)
    elif action == "Update":
        Update(direction,value)
    elif action == "Delete":
        Delete(direction)
    elif action == "Read":
        Read(direction)





