def calculate_pos(mat,row,col):
    if row < 0:
        row = len(mat) -1
    if col < 0:
        col = len(mat) - 1
    if row >= len(mat):
        row = 0
    if col >= len(mat):
        col = 0

    return row,col

n = int(input())

matrix = []
player_pos = []
for row in range(n):
    row_data = input().split(' ')
    if 'P' in row_data:
        player_pos = [row,row_data.index('P')]
    matrix.append(row_data)

player_path = []



# directions = { #TODO
#     "up":(1,0),
#     "down":(-1,0),
#     "left":(0,-1),
#     "right":(0,1),
# }
coins_collected = 0
is_winner = True
player_path.append(player_pos)
while coins_collected < 100:

    command = input()

    # player_pos += directions[command]
    current_row,current_col = player_pos
    if command == "up":
        row,col = calculate_pos(matrix,current_row-1,current_col)

    elif command == "down":
        row,col = calculate_pos(matrix,current_row+1,current_col)

    elif command == "left":
        row,col = calculate_pos(matrix,current_row,current_col - 1)

    elif command == "right":
        row,col = calculate_pos(matrix,current_row,current_col+1)

    matrix[current_row][current_col] = '0'
    if matrix[row][col] == 'X':
        player_path.append([row,col])
        is_winner = False
        coins_collected //=2
        print(f"Game over! You've collected {coins_collected } coins.")
        break

    coins_collected += int(matrix[row][col])
    matrix[row][col] = 'P'
    player_pos = [row,col]
    player_path.append(player_pos)

if is_winner:
    print(f"You won! You've collected {coins_collected} coins.")
print(f'Your path:')
[print(step) for step in player_path]

