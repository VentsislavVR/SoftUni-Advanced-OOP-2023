from collections import deque

quantity_of_food=int(input())

orders = deque([int(x) for x in input().split()])
print(max(orders))

while quantity_of_food >0 and orders:
    cur_order = orders[0]

    if quantity_of_food >= cur_order:
        quantity_of_food -= cur_order
        orders.popleft()
    else:
        break
if orders:
    print(f'Orders left: {" ".join(str(x)for x in orders)}')
else:
    print('Orders complete')







