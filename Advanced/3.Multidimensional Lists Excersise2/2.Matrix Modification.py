rows = int(input())

matrix = [[int(x) for x in input().split()] for i in range(rows)]


while True:
    command = input().split()
    if command[0] == 'END':
        break
    symbol,row,col,value = command
    if int(row) < 0 or int(col) < 0 or int(row) >= rows or int(col) >= rows :
        print('Invalid coordinates')
        continue

    if symbol == 'Add':
        matrix[int(row)][int(col)] += int(value)
    if symbol == 'Subtract':
        matrix[int(row)][int(col)] -= int(value)

[print(*x) for x in matrix]