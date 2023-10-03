from collections import deque

line = deque(input().split())
number = deque()

operators = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x // y
}
for i in line:
    if i not in '+-*/':
        number.append(int(i))
    else:
        while len(number) > 1:
            number.appendleft(operators[i](int(number.popleft()),int(number.popleft())))
print(*number)