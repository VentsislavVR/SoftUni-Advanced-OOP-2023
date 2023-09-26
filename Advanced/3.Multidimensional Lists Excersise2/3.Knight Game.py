# size = int(input())
# matrix = [list(input()) for _ in range(size)]
# # a = [-2, -1, 1, 2 ]
# # positions = [(x,y) for x in a for y in a if abs(x) != abs(y)]
# positions = ( # all valid horse moves !
#     (2, 1),  # two down one right.
#     (2, -1),  # two down one left .
#     (-1, 2),  # two right one up.
#     (1, 2),   # two right one down.
#     (-2, -1), # two up one left.
#     (-2, 1),  # two up one right.
#     (-1, -2), # two left one up.
#     (1, -2),  # two left one down.
# )

n = int(input())
matrix = []
knights = []

for row in range(n):
    matrix.append([x for x in input()])
    for col in range(n):
        if matrix[row][col] == 'K':
            knights.append([row, col])
removed_knights = 0

possible_moves = [(1,2),(2,1),
                  (-1,2),(-2,1),
                  (1,-2),(2,-1),
                  (-1,-2),(-2,-1)
                  ]


while True:
    max_hits = 0
    max_knights = [0,0]
    for k_row,k_col in knights:
        hits = 0
        for m_row,m_col in possible_moves:
            new_row = k_row + m_row
            new_col = k_col + m_col
            if new_row >= 0 and new_row < n and new_col >= 0 and new_col < n:
                if matrix[new_row][new_col] == 'K':
                    hits += 1
        if hits > max_hits:
            max_hits = hits
            max_knights = [k_row,k_col]

    if max_hits == 0:
        break

    knights.remove(max_knights)
    matrix[max_knights[0]][max_knights[1]] = '0'
    removed_knights += 1

print(removed_knights)
