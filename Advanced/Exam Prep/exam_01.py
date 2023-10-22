from collections import deque


initial_fuel = deque([int(x) for x in input().split()])
additional_consumption_index = deque([int(x) for x in input().split()])

needed_fuel_amount = deque([int(x) for x in input().split()])
altetute_count = 0

while True:
    cur_fuel = initial_fuel[-1]
    cur_consumption = additional_consumption_index[0]
    cur_needed_fuel = needed_fuel_amount[0]

    cur_sum = cur_fuel - cur_consumption

    if cur_sum >= cur_needed_fuel:
        initial_fuel.pop()
        additional_consumption_index.popleft()
        needed_fuel_amount.popleft()
        altetute_count += 1
        print(f"John has reached: Altitude {altetute_count}")
    else:
        print(f"John did not reach: Altitude {altetute_count +1 }")
        break

if len(needed_fuel_amount) >0:
    if altetute_count > 0:
        print(f"John failed to reach the top.")
        res = f'Reached altitudes: '
        for i in range(1,altetute_count+1):
            res += f'Altitude {i}'
            res += ', '
        print(res[:-2])
    else:
        print(f"John failed to reach the top.\nJohn didn't reach any altitude.")
else:
    print("John has reached all the altitudes and managed to reach the top!")


