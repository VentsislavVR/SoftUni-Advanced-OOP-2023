from collections import deque

line = deque(input().split())
number = deque()

for i in line:
    if i not in '+-*/':
        number.append(int(i))
    else:
        while len(number) > 1:
            if i == '*':
                number.appendleft(int(number.popleft()) * int(number.popleft()))
            elif i == '/':
                number.appendleft(int(number.popleft()) // int(number.popleft()))
            elif i == '+':
                number.appendleft(int((number.popleft()) + int(number.popleft())))
            elif i == '-':
                number.appendleft(int(number.popleft()) - int(number.popleft()))

print(*number)