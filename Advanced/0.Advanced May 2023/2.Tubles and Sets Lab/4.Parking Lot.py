n = int(input())
cars = set()

for car in range(n):
    direction,number = input().split(', ')

    if direction == 'IN':
        if number not in cars:
            cars.add(number)

    else:
        cars.remove(number)

if not cars:
    print(f"Parking Lot is Empty")
else:
    print('\n'.join(cars))


