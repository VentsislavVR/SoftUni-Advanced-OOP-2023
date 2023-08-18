SIZE = 6

matrix = []

for row in range(SIZE):
    line = input().split()
    if "E" in line:
        rover_position = [row, line.index("E")]

    matrix.append(line)

commands = input().split(", ")

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

deposits = {
    "W": 0,
    "M": 0,
    "C": 0,
}

deposits_full_name = {
    "W":"Water",
    "M":"Metal",
    "C":"Concrete",

}

while commands:
    command = commands.pop(0)

    rover_position[0] = rover_position[0] + directions[command][0]
    rover_position[1] = rover_position[1] + directions[command][1]

    for i in range(len(rover_position)):
        if rover_position[i] < 0:
            rover_position[i] = SIZE - 1
        elif rover_position[i] == SIZE:
            rover_position[i] = 0

    position = matrix[rover_position[0]][rover_position[1]]

    if position == "W" or position == "M" or position == "C":
        deposits[position] += 1
        print(f"{deposits_full_name[position]} deposit found at ({rover_position[0]}, {rover_position[1]})") # maybe rover pos 0,1

    elif position == "R":
        print(f"Rover got broken at ({rover_position[0]}, {rover_position[1]})") # maybe rov pos 0,1
        break

if all(deposits.values()):
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")


