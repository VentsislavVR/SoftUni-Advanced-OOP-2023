matrix = []

# for i in range(6):
#     matrix.append(input().split())
for i in range(6):
    line = list(input().split())
    matrix.append(line)

position = input()
row = int(position[1])
col = int(position[4])


command = input()

while command != "Stop":

    command_elements = command.split(", ")
    action = command_elements[0]
    direction = command_elements[1]

    if direction == "up":
        row -= 1
    if direction == "down":
        row += 1
    if direction == "left":
        col -= 1
    if direction == "right":
        col += 1

    if action == "Create":
        value = command_elements[2]
        if matrix[row][col] == ".":
            matrix[row][col] = value
    if action == "Update":
        value = command_elements[2]
        if matrix[row][col] != ".":
            matrix[row][col] = value

    if action == "Delete":
        matrix[row][col] = "."
    if action == "Read":
        if matrix[row][col] != ".":
            print(matrix[row][col])


    command = input()

for row in matrix:
    print(' '.join(row))