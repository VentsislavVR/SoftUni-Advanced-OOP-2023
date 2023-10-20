from collections import deque

players = deque(input().split(", "))

matrix = [[int(x) if x.isdigit() else str(x) for x in input().split()] for row in range(7)]

players_scores = {
    players[0]: [501,0],
    players[1]: [501,0],
}


current_player = players[0]

while True:
    throws = input().strip('()').replace(' ', '').split(',')
    row, col = [int(x) for x in throws]
    players_scores[current_player][1] += 1
    if row in range(7) and col in range(7):
        if matrix[row][col] == "D":
            players_scores[current_player][0] -= (matrix[row][0] + matrix[row][-1] + matrix[0][col] + matrix[-1][col]) * 2

        elif matrix[row][col] == "T":
            players_scores[current_player][0] -= (matrix[row][0] + matrix[row][-1] + matrix[0][col] + matrix[-1][col]) * 3

        elif matrix[row][col] == "B":
            print(f"{current_player} won the game with {players_scores[current_player][1]} throws!")
            break
        else:
            players_scores[current_player][0] -= matrix[row][col]
    else:
        players.rotate()
        current_player = players[0]
        continue

    if players_scores[current_player][0] <= 0:
        print(f"{current_player} won the game with {players_scores[current_player][1]} throws!")
        break

    players.rotate()
    current_player = players[0]
