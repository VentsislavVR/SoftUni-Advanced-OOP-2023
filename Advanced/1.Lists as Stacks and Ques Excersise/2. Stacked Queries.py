from collections import deque
numbers = deque()

mapper = {
    1:lambda x:numbers.append(x[1]),
    2:lambda x:numbers.pop() if numbers else None,
    3:lambda x:print(max(numbers)) if numbers else None,
    4:lambda x:print(min(numbers)) if numbers else None
}
n = int(input())
for i in range(n):
    data = [int(x) for x in input().split()]
    mapper[data[0]](data)

numbers.reverse()
print(*numbers, sep=", ")