
def check_valid_index(row, col):
    if 0 <= row < size and 0 <= col < size:
        return True
    return False

def create_matrix(size):
    matrix = []
    first_tunel_coordinates = []
    second_tunel_coordinates = []
    snake = []
    first_found = False
    for row in range(size):
        matrix.append(list(input()))
        for col in range(size):
            if matrix[row][col] == 'S':
                snake = [row, col]
                matrix[row][col] = '.'

            if matrix[row][col] == 'B':
                if first_found:
                    second_tunel_coordinates = [row, col]
                else:
                    first_tunel_coordinates = [row, col]
                    first_found = True



    return matrix,first_tunel_coordinates,second_tunel_coordinates,snake

size = int(input())
matrix,first_tunnel,second_tunnel ,snake_pos= create_matrix(size)

directions = {
    'up':(-1,0),
    'down':(1,0),
    'left':(0,-1),
    'right':(0,1),

}

food_quantity = 0
while True:
    command = input()
    snake_row = snake_pos[0] + directions[command][0]
    snake_col = snake_pos[1] + directions[command][1]

    if not check_valid_index(snake_row, snake_col):
        print("Game over!")
        break

    if matrix[snake_row][snake_col] == '*':
        food_quantity += 1
        matrix[snake_row][snake_col] = '.'
        if food_quantity == 10:
            print('You won! You fed the snake.')
            matrix[snake_row][snake_col] = 'S'
            break

    if matrix[snake_row][snake_col] == 'B':
        if tuple(snake_pos) == first_tunnel:
            matrix[second_tunnel[0]][second_tunnel[1]] = '.'
            matrix[first_tunnel[0]][first_tunnel[1]] = '.'
            snake_pos = [first_tunnel[0], first_tunnel[1]]
            continue

        else:
            matrix[first_tunnel[0]][first_tunnel[1]] = '.'
            matrix[second_tunnel[0]][second_tunnel[1]] = '.'
            snake_pos = [second_tunnel[0], second_tunnel[1]]
            continue
    matrix[snake_row][snake_col] = '.'

    snake_pos[0] = snake_row
    snake_pos[1] = snake_col




print(f"Food eaten: {food_quantity}")
# print(*['\n'.join(str(x) for x in matrix)])
[print(*row,sep='') for row in matrix]

