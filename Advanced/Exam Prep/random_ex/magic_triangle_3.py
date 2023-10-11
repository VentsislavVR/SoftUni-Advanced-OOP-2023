def get_magic_triangle(n):
    if n < 1:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle

n = 5
magic_triangle = get_magic_triangle(n)

print(magic_triangle)
