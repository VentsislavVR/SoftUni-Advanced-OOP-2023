from collections import deque

available_seats = input().split(", ")

first_sequence = deque([int(x) for x in input().split(", ")])
second_sequence = deque([int(x) for x in input().split(", ")])


rotations = 0
matched = []
while len(matched) < 3 and rotations < 10:
    rotations += 1
    first = first_sequence.popleft()
    second= second_sequence.pop()


    letter = chr(first + second)

    first_opt = str(first )+ letter
    second_opt = str(second) + letter

    if first_opt in matched or second_opt in matched:
        continue
    if first_opt in available_seats:
        matched.append(first_opt)
        continue
    if second_opt in available_seats:
        matched.append(second_opt)
        continue

    first_sequence.append(first)
    second_sequence.appendleft(second)


print(f"Seat matches: {', '.join(matched)}")
print(f"Rotations count: {rotations}")


























