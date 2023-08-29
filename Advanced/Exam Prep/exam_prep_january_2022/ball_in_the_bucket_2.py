SIZE = 6

matrix = [input().split() for _ in range(SIZE)]

total_points = 0
throws_count = 3

for throw in range(throws_count):
    row, col = [int(el) for el in eval(input())]
    try:
        if matrix[row][col] == 'B':
            total_points += sum(
                [int(matrix[row_index][col]) for row_index in range(SIZE) if matrix[row_index][col].isdigit()])
    except IndexError:
        continue
prize = ''
if 100 <= total_points <= 199:
    prize = 'Football'
elif 199 < total_points <= 299:
    prize = 'Teddy Bear'
elif total_points > 299:
    prize = 'Lego Construction Set'

if prize:
    print(f"Good job! You scored {total_points} points, and you've won {prize}.")
else:
    print(f"Sorry! You need {100 - total_points} points more to win a prize.")
