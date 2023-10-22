
SIZE = int(input())
matrix = []

boat_pos = []
for rows in range(SIZE):
    matrix.append(list(input()))
    if 'S' in matrix[rows]:
        boat_pos = [rows, matrix[rows].index('S')]
        matrix[rows][matrix[rows].index('S')] = '-'

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

fish_amount = 0
whirpool = False
while True:
    command = input()
    if command == 'collect the nets':
        matrix[boat_pos[0]][boat_pos[1]] = 'S'
        if fish_amount >= 20:
            print("Success! You managed to reach the quota!")
            break
        else:
            print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - fish_amount} tons of fish more.")

            break
    cur_row = boat_pos[0] + directions[command][0]
    cur_col = boat_pos[1] + directions[command][1]

    cur_row %= SIZE
    cur_col %= len(matrix[0])


    if matrix[cur_row][cur_col] == 'W':
        fish_amount = 0
        whirpool = True
        matrix[cur_row][cur_col] = '-'
        break

    if matrix[cur_row][cur_col].isdigit():
        fish_amount += int(matrix[cur_row][cur_col])
        matrix[cur_row][cur_col] = '-'

    boat_pos = [cur_row, cur_col]

if fish_amount > 0:
    print(f"Amount of fish caught: {fish_amount} tons.")
if whirpool:
    print(
        f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{cur_row},{cur_col}]")
else:
    [print(''.join(x)) for x in matrix]

