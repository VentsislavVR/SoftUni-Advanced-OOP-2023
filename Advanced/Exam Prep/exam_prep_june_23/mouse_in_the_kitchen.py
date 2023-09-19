rows, cols = [int(x) for x in input().split(',')]
matrix = [list(input()) for _ in range(rows)]


def find_mouse_position(matrix):
    for row in range(rows):
        if 'M' in matrix[row]:
            return row, matrix[row].index('M')


mouse_pos_row,mouse_pos_col = find_mouse_position(matrix)
matrix[mouse_pos_row][mouse_pos_col] = '*'

mouse_movement = [[mouse_pos_row,mouse_pos_col]]


directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}


def check_valid_index(row, col):
    if 0 <= row < rows and 0 <= col < cols:
        return True
    return False


def find_cheese(matrix):
    cheese = 0
    for row in matrix:
        for col in row:
            if col == 'C':
                cheese += 1
    return cheese


cheese_count = find_cheese(matrix)
eaten_cheese = 0

while True:

    command = input()
    last_row = mouse_movement[-1][0]
    last_col = mouse_movement[-1][1]
    if command == 'danger':
        if eaten_cheese < cheese_count:
            matrix[mouse_move_row][mouse_move_col] = ' '
            print("Mouse will come back later!")
        break


    mouse_move_row, mouse_move_col = directions[command][0] + mouse_pos_row, directions[command][1] + \
                                     mouse_pos_col

    if not check_valid_index(mouse_move_row, mouse_move_col):
        matrix[last_row][last_col] = 'M'
        print("No more cheese for tonight!")
        break
    mouse_movement.append([mouse_move_row, mouse_move_col])

    if matrix[mouse_move_row][mouse_move_col] == 'C':
        matrix[mouse_move_row][mouse_move_col] = '*'
        eaten_cheese += 1
        if eaten_cheese == cheese_count:
            matrix[mouse_move_row][mouse_move_col] = 'M'
            print("Happy mouse! All the cheese is eaten, good night!")
            break
    if matrix[mouse_move_row][mouse_move_col] == 'T':
        matrix[mouse_move_row][mouse_move_col] = 'M'
        print("Mouse is trapped!")
        break
    if matrix[mouse_move_row][mouse_move_col] == '@':

        continue



    mouse_pos_row,mouse_pos_col = mouse_move_row,mouse_move_col


[print(*row,sep='') for row in matrix]
