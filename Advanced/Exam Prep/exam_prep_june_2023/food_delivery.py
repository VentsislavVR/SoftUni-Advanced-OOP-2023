rows, cols = [int(x) for x in input().split()]

matrix = [list(input()) for _ in range(rows)]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

def find_boy_pos(matrix):
    for row in range(rows):
        if 'B' in matrix[row]:
            return row, matrix[row].index('B')

def check_valid_index(row, col):
    if 0 <= row < rows and 0 <= col < cols:
        return True

boy_row, boy_col = find_boy_pos(matrix)
boy_start_row, boy_start_col = boy_row, boy_col

while True:
    command = input()
    if not command:
        break
    player_moves_row, player_moves_col = boy_row + directions[command][0], boy_col + directions[command][1]
    if not check_valid_index(player_moves_row, player_moves_col):
        print("The delivery is late. Order is canceled.")
        matrix[boy_start_row][boy_start_col] = ' '
        break

    if matrix[player_moves_row][player_moves_col] == 'P':
        matrix[player_moves_row][player_moves_col] = 'R'
        print("Pizza is collected. 10 minutes for delivery.")


    if matrix[player_moves_row][player_moves_col] == '*':
        continue

    if matrix[player_moves_row][player_moves_col] == "A":
        matrix[player_moves_row][player_moves_col] = "P"
        print("Pizza is delivered on time! Next order...")
        break
    if matrix[player_moves_row][player_moves_col] not in ('A','P','R','B',):
        matrix[player_moves_row][player_moves_col] = '.'
    boy_row, boy_col = player_moves_row, player_moves_col

[print(*row, sep='') for row in matrix]
