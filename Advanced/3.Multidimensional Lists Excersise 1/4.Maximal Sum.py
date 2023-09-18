rows,cols = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for row in range(rows)]

max_sum = float('-inf')

biggest_matrix = []

for row in range(rows-2):
    for col in range(cols-2):
        first_row = matrix[row][col:col+3]
        second_row = matrix[row+1][col:col+3]
        third_row = matrix[row+2][col:col + 3]

        curren_sum = sum(first_row)+sum(second_row)+sum(third_row)

        if curren_sum > max_sum:
            max_sum = curren_sum
            biggest_matrix =[first_row,second_row,third_row]

print(f'Sum = {max_sum}')
[print(*row) for row in biggest_matrix]
