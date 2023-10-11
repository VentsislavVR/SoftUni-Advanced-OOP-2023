from collections import deque
# def list_manipulator(*args):
#     result = deque(args[0])
#     if len(args) == 3:
#
#         first_command = args[1]
#         second_command = args[2]
#         numbers = False
#     else:
#         first_command = args[1]
#         second_command = args[2]
#         numbers = [x for x in args[3:]]
#
#     if first_command == 'add':
#         if second_command == 'beginning':
#             result.insert(0,numbers)
#
#         elif second_command == 'end':
#             result.extend(numbers)
#     if first_command == 'remove':
#         if second_command == 'beginning':
#             if numbers:
#                 for i in range(numbers[0]):
#                     result.popleft()
#             else:
#                 result.popleft()
#         if second_command == 'end':
#             if numbers:
#                 for i in range(numbers[0]):
#                     result.pop()
#             else:
#                 result.pop()
#
#
#
#     result = [x for item in result for x in (item if isinstance(item, list) else [item])]
#     return result
from collections import deque

def list_manipulator(data, command, position, *args):
    data = deque(data)
    data.extendleft(reversed(args)) if command == 'add' and position == 'beginning' else data.extend(args) if command == 'add' and position == 'end' else (data.popleft() if not args else [data.popleft() for _ in range(args[0])]) if command == 'remove' and position == 'beginning' else (data.pop() if not args else [data.pop() for _ in range(args[0])]) if command == 'remove' and position == 'end' else None
    return list(data)



print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
