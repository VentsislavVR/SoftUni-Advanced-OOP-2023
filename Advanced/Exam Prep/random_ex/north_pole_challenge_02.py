rows, cols = [int(x) for x in input().split(', ')]
matrix = []
santa_position = []
santas_bag = {
    'Christmas decorations': 0,
    'Gifts': 0,
    'Cookies': 0,
}
to_be_collected_gifts = 0
to_be_collected_cookies = 0
to_be_collected_decoration = 0

for row_index in range(rows):
    row_data = list(input().split(' '))
    if 'Y' in row_data:
        col_index = row_data.index('Y')
        santa_position = [row_index, col_index]
    if 'G' in row_data:
        to_be_collected_gifts += row_data.count('G')
    if 'C' in row_data:
        to_be_collected_cookies += row_data.count('C')
    if 'D' in row_data:
        to_be_collected_decoration += row_data.count('D')

    matrix.append(row_data)

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

mc = False
while not mc:
    command = input().split('-')

    if mc or command[0] == 'End':
        matrix[santa_position[0]][santa_position[1]] = 'Y'
        break

    direction = command[0]
    step = int(command[1])
    matrix[santa_position[0]][santa_position[1]] = 'x'

    for i in range(step):
        current_row = (santa_position[0] + directions[direction][0]) % rows
        current_col = (santa_position[1] + directions[direction][1]) % cols


        if matrix[current_row][current_col] == 'D':
            santas_bag['Christmas decorations'] += 1
            matrix[current_row][current_col] = '-'
        elif matrix[current_row][current_col] == 'G':
            santas_bag['Gifts'] += 1
            matrix[current_row][current_col] = '-'
        elif matrix[current_row][current_col] == 'C':
            santas_bag['Cookies'] += 1
        if (
            santas_bag['Gifts'] == to_be_collected_gifts
            and santas_bag['Cookies'] == to_be_collected_cookies
            and santas_bag['Christmas decorations'] == to_be_collected_decoration
        ):
            print('Merry Christmas!')
            mc = True
            santa_position = [current_row, current_col]
            break

        matrix[current_row][current_col] = 'x'
        santa_position = [current_row, current_col]

matrix[santa_position[0]][santa_position[1]] = 'Y'
print("You've collected:")
for key, value in santas_bag.items():
    print(f'- {value} {key}')

for row in matrix:
    print(' '.join(row))
