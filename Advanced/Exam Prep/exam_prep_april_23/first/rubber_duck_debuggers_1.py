from collections import deque
programmer_time = deque(int(x) for x in input().split())
programmer_tasks = [int(x) for x in input().split()]
ducks = {
    range(181, 240 + 1): 'Small Yellow Rubber Ducky',
    range(121, 180 + 1): 'Big Blue Rubber Ducky',
    range(61, 120 + 1): 'Thor Ducky',
    range(0, 60 + 1): 'Darth Vader Ducky',
}
duckies_counter = {
    'Darth Vader Ducky': 0,
    'Thor Ducky': 0,
    'Big Blue Rubber Ducky': 0,
    'Small Yellow Rubber Ducky': 0,
}
max_range = 240
while programmer_tasks and programmer_time:
    time = programmer_time.popleft()
    task = programmer_tasks.pop()

    current_sum = time * task
    if current_sum > max_range:
        programmer_time.append(time)
        programmer_tasks.append(task-2)

    for d in ducks:
        if current_sum in d:
            duckies_counter[ducks[d]]+=1
            break
res = ["Congratulations, all tasks have been completed! Rubber ducks rewarded:\n"]
res.append('\n'.join([f'{duck}: {count}' for duck,count in duckies_counter.items()]).lstrip(' '))
print(*res)