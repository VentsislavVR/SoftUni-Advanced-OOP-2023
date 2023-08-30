import re


def is_inside(size, row, col):
    return 0 <= row < size and 0 <= col < size


def count_neighbour_bombs(game_field, row, col):
    count = 0
    if is_inside(len(game_field), row - 1, col) and game_field[row - 1][col] == '*':
        count += 1
    if is_inside(len(game_field), row + 1, col) and game_field[row + 1][col] == '*':
        count += 1
    if is_inside(len(game_field), row, col - 1) and game_field[row][col - 1] == '*':
        count += 1
    if is_inside(len(game_field), row, col + 1) and game_field[row][col + 1] == '*':
        count += 1

    if is_inside(len(game_field), row - 1, col - 1) and game_field[row - 1][col - 1] == '*':
        count += 1

    if is_inside(len(game_field), row - 1, col + 1) and game_field[row - 1][col + 1] == '*':
        count += 1
    if is_inside(len(game_field), row + 1, col - 1) and game_field[row + 1][col - 1] == '*':
        count += 1
    if is_inside(len(game_field), row + 1, col + 1) and game_field[row + 1][col + 1] == '*':
        count += 1

    return count


game_field_size = int(input())

game_field = []

for _ in range(game_field_size):
    game_field.append([None] * game_field_size)

bombs_count = int(input())

for _ in range(bombs_count):
    row, col = [int(x) for x in re.findall('\\d+', input())]

    game_field[row][col] = '*'

for row in range(game_field_size):
    for col in range(game_field_size):
        if game_field[row][col] == '*':
            continue

        cell_value =count_neighbour_bombs(game_field, row, col)
        game_field[row][col] = cell_value

for row in game_field:
    print(*row,sep=' ')