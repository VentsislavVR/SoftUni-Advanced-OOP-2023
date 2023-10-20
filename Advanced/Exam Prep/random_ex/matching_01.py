from collections import deque

males = deque([int(x) for x in input().split()])
females = deque([int(x) for x in input().split()])
matches = 0

while males and females:
    cur_m = males[-1]
    cur_f = females[0]
    if cur_m <= 0:
        males.pop()
        continue
    elif cur_f <= 0:
        females.popleft()
        continue

    elif cur_m % 25 == 0:
        males.pop()
        males.pop()

    elif cur_f % 25 == 0:
        females.popleft()
        females.popleft()

    elif cur_m == cur_f:
        matches += 1
        males.pop()
        females.popleft()
    else:
        females.popleft()
        males[-1] -= 2
        # males.appendleft(males.pop()-2)


print(f"Matches: {matches}")
print(f"Males left: {', '.join([str(x) for x in reversed(males)])}" if males else f"Males left: none")
print(f"Females left: {', '.join([str(x) for x in females])}" if females else f"Females left: none")


from collections import deque

def match_people(males, females):
    matches = 0
    while males and females:
        cur_m = males[-1]
        cur_f = females[0]

        if cur_m <= 0:
            males.pop()
        elif cur_f <= 0:
            females.popleft()
        elif cur_m % 25 == 0:
            males.pop()
            males.pop()
        elif cur_f % 25 == 0:
            females.popleft()
            females.popleft()
        elif cur_m == cur_f:
            males.pop()
            females.popleft()
            matches += 1
        else:
            females.popleft()
            males[-1] -= 2

    return males, females, matches
males = deque([int(x) for x in input().split()])
females = deque([int(x) for x in input().split()])

males, females,matches = match_people(males, females)
print(f"Matches: {matches}")
print(f"Males left: {', '.join([str(x) for x in reversed(males)])}" if males else f"Males left: none")
print(f"Females left: {', '.join([str(x) for x in females])}" if females else f"Females left: none")

