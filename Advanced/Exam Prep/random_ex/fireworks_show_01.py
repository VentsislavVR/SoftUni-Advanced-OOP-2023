from collections import deque

effects = deque([int(x) for x in input().split(', ')])
power = [int(x) for x in input().split(', ')]

fireworks = {
    'Palm Fireworks': 0,
    'Willow Fireworks': 0,
    'Crossette Fireworks': 0,
}
victory = False

while True:
    if all(count >= 3 for count in fireworks.values()):
        victory = True
        break

    if not effects or not power:
        break

    cur_effect = effects[0]
    cur_power = power[-1]

    if cur_effect <= 0:
        effects.popleft()
        continue
    if cur_power <= 0:
        power.pop()
        continue

    cur_sum = cur_effect + cur_power

    if cur_sum % 3 == 0 and cur_sum % 5 != 0:
        fireworks['Palm Fireworks'] += 1
        effects.popleft()
        power.pop()
    elif cur_sum % 5 == 0 and cur_sum % 3 != 0:
        fireworks['Willow Fireworks'] += 1
        effects.popleft()
        power.pop()
    elif cur_sum % 3 == 0 and cur_sum % 5 == 0:
        fireworks['Crossette Fireworks'] += 1
        effects.popleft()
        power.pop()
    else:
        effects.popleft()
        effects.append(cur_effect - 1)

result_lines = []

if victory:
    result_lines.append('Congrats! You made the perfect firework show!')
else:
    result_lines.append("Sorry. You can't make the perfect firework show.")

if effects:
    result_lines.append(f'Firework Effects left: {", ".join(map(str, effects))}')
if power:
    result_lines.append(f'Explosive Power left: {", ".join(map(str, power))}')

for firework, count in fireworks.items():
    result_lines.append(f'{firework}: {count}')

print('\n'.join(result_lines))
