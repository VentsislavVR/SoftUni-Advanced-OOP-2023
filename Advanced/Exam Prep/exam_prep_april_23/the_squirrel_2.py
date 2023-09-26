
goal = 3
hazelnuts = 0
hamster_pos = []
matrix = []
victory = False
alive = True
n = int(input())
commands = input().split(', ')
for row in range(n):
    matrix.append(list(input()))
    for col in range(n):
        if matrix[row][col] == 's':
            hamster_pos = [row, col]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}
for move in commands:
    r = hamster_pos[0] + directions[move][0]
    c = hamster_pos[1] + directions[move][1]

    if r < 0 or r >= n or c < 0 or c >= n:
        print("The squirrel is out of the field.")
        alive = False
        break

    if matrix[r][c] == 't':
        print("Unfortunately, the squirrel stepped on a trap...")
        alive = False
        break

    if matrix[r][c] == 'h':
        hazelnuts += 1
        matrix[r][c] = '*'
        if hazelnuts == goal:
            victory = True
            print("Good job! You have collected all hazelnuts!")
            break


    hamster_pos = [r, c]

if not victory and alive:
    print("There are more hazelnuts to collect.")
print(f"Hazelnuts collected: {hazelnuts}")




# def initialize_matrix(n):
#     matrix = []
#     hamster_pos = None
#     for _ in range(n):
#         row = list(input())
#         if 's' in row:
#             hamster_pos = [_, row.index('s')]
#         matrix.append(row)
#     return matrix, hamster_pos
#
#
# def is_valid_move(r, c, n):
#     return 0 <= r < n and 0 <= c < n
#
#
# def main():
#     goal = 3
#     hazelnuts = 0
#     victory = False
#     alive = True
#
#     n = int(input())
#     commands = input().split(', ')
#
#     matrix, hamster_pos = initialize_matrix(n)
#
#     directions = {
#         'up': (-1, 0),
#         'down': (1, 0),
#         'left': (0, -1),
#         'right': (0, 1)
#     }
#
#     for move in commands:
#         dr, dc = directions[move]
#         r, c = hamster_pos[0] + dr, hamster_pos[1] + dc
#
#         if not is_valid_move(r, c, n):
#             print("The squirrel is out of the field.")
#             alive = False
#             break
#
#         cell = matrix[r][c]
#         if cell == 't':
#             print("Unfortunately, the squirrel stepped on a trap...")
#             alive = False
#             break
#         elif cell == 'h':
#             hazelnuts += 1
#             if hazelnuts == goal:
#                 victory = True
#                 print("Good job! You have collected all hazelnuts!")
#                 break
#
#         hamster_pos = [r, c]
#
#     if alive and not victory:
#         print("There are more hazelnuts to collect.")
#     print(f"Hazelnuts collected: {hazelnuts}")
#
#
# if __name__ == "__main__":
#     main()

