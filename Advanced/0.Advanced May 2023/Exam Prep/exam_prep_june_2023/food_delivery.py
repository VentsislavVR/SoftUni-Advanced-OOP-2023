rows, cols = [int(x) for x in input().split(' ')]

matrix = []
delivery_boy_pos = []
for row in range(rows):
    line = input().strip()
    if 'B' in line:
        delivery_boy_pos = [row, line.index('B')]
    matrix.append(line.split())

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}





