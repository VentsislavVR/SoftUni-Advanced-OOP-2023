from collections import deque

eggs =deque(input().split(", "))
wraps = deque(input().split(", "))
BOX_SIZE = 50
box_count = 0

while eggs and wraps:
    current_egg = int(eggs[0])
    current_wrap = int(wraps[-1])

    if current_egg <= 0:
        eggs.popleft()
        continue
    if current_egg == 13:
        eggs.popleft()
        wraps[0],wraps[-1] = wraps[-1], wraps[0]
        continue

    eggs.popleft()
    wraps.pop()

    if current_egg + current_wrap <= BOX_SIZE:
        box_count += 1
        continue

if box_count > 0:
    print(f"Great! You filled {box_count} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join(eggs)}")
if wraps:
    print(f"Pieces of paper left: {', '.join(wraps)}")







