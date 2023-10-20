text = input()

SIZE = int(input())

matrix = []
player_pos = []
for rows in range(SIZE):
    matrix.append(list(input()))
    if 'P' in matrix[rows]:
        player_pos = [rows, matrix[rows].index('P')]
        matrix[rows][matrix[rows].index('P')] = '-'

command_count = int(input())
commands = [[x for x in input().split()] for i in range(command_count)]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}


def check_valid_pos(row, col, SIZE):
    if 0 <= row < SIZE and 0 <= col < SIZE:
        return True
    return False



for command in commands:
    last_pos = player_pos.copy()
    player_pos[0] += directions[command[0]][0]
    player_pos[1] += directions[command[0]][1]
    if check_valid_pos(player_pos[0],player_pos[1],SIZE):
        if matrix[player_pos[0]][player_pos[1]] != '-':
            text += matrix[player_pos[0]][player_pos[1]]
            matrix[player_pos[0]][player_pos[1]] = '-'
    else:
        if text:
            text = text[:-1]
        player_pos = last_pos.copy()


matrix[player_pos[0]][player_pos[1]] = 'P'

print(text)
[print(''.join(x)) for x in matrix]