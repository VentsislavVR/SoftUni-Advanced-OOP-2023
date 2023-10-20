from collections import deque


tools = deque([int(x) for x in input().split()])
substances = [int(x) for x in input().split()]

challenges = [int(x) for x in input().split()]

while tools and substances and challenges:
    tool = tools[0]
    substance= substances[-1]


    if tool * substance in challenges:
        challenges.__delitem__(challenges.index(tool*substance))
        tools.popleft()
        substances.pop()
    else:
        tool += 1
        tools.append(tool)
        tools.popleft()
        substance -= 1
        substances.pop()
        if substance >0:
            substances.append(substance)

if challenges:
    print("Harry is lost in the temple. Oblivion awaits him.")
if not challenges:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")

if tools:
    print(f"Tools: {', '.join([str(x)for x in tools])}")
if substances:
    print(f"Substances: {', '.join([str(x)for x in substances])}")
if challenges:
    print(f"Challenges: {', '.join([str(x)for x in challenges])}")


