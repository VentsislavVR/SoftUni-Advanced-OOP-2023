rows,cols = [int(x) for x in input().split()]


start = ord('a')


for row in range(rows):
    middle = start
    for col in range(cols):
        print(f'{chr(start)}{chr(middle)}{chr(start)}',end=' ')
        middle += 1
    print()
    start += 1






