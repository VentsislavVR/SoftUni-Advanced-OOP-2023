n = int(input())
matrix = [[int(x) for x in input().split(' ')] for row in range(n)]

primary = 0
secondary = 0

for i in range(n):
    primary += matrix[i][i]
    secondary += matrix[i][n - 1 - i]
print(abs(primary - secondary))

