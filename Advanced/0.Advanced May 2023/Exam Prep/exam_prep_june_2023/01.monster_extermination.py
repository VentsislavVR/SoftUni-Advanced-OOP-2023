from collections import deque

monster_armor = deque([int(x) for x in input().split(',')])
soldier_power = [int(x) for x in input().split(',')]
kill_streak = 0
while monster_armor and soldier_power:

    monster = monster_armor.popleft()
    soldier = soldier_power.pop()

    if soldier >= monster:
        soldier -= monster
        kill_streak += 1
        if soldier_power:
            soldier_power[-1] += soldier
        elif not soldier_power and soldier > 0:
            soldier_power.append(soldier)

    elif soldier < monster:
        monster -= soldier
        monster_armor.append(monster)

if not monster_armor:
    print(f"All monsters have been killed!")
if not soldier_power:
    print('The soldier has been defeated.')
print(f"Total monsters killed: {kill_streak}")
