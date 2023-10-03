n, m = map(int, input().split())


matrix = []
my_pos = []

for row in range(n):
    matrix.append(list(input().split()))
    if 'B' in matrix[row]:
        my_pos = [row, matrix[row].index('B')]
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}
made_moves = 0
touched_opponents = 0
while True:
    if touched_opponents == 3 :
        break
    command = input()
    if command == 'Finish':

        break
    r = my_pos[0] + directions[command][0]
    c = my_pos[1] + directions[command][1]
    if (r < 0 or r >= n or c < 0 or c >= n) or matrix[r][c] == 'O':
        continue

    if matrix[r][c] == 'P':
        touched_opponents += 1
        made_moves += 1
        matrix[r][c] = '-'
        my_pos = [r, c]
        continue
    made_moves += 1
    my_pos = [r, c]

print('Game over!')
print(f"Touched opponents: {touched_opponents} Moves made: {made_moves}")
