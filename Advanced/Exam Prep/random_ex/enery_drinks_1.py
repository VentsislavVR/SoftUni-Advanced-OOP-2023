from collections import deque

mg_coffe = [int(x) for x in input().split(',')]
energy_drinks = deque([int(x) for x in input().split(',')])

maximum_caffeine = 300
initial_caffeine = 0

while mg_coffe and energy_drinks:
    caffeine_total = mg_coffe[-1] * energy_drinks[0]

    if caffeine_total + initial_caffeine <= maximum_caffeine:
        initial_caffeine += caffeine_total
        mg_coffe.pop()
        energy_drinks.popleft()
    else:
        mg_coffe.pop()
        energy_drinks.append(energy_drinks.popleft())
        initial_caffeine -= 30
        if initial_caffeine < 0:
            initial_caffeine = 0

print(f"Drinks left: {', '.join(str(x) for x in energy_drinks)}"if energy_drinks else 'At least Stamat wasn\'t exceeding the maximum caffeine.')
print(f"Stamat is going to sleep with { initial_caffeine} mg caffeine.")

