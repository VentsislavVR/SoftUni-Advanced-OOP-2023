from collections import deque

pizza_orders = deque(int(x) for x in input().split(', '))
employees = [int(x) for x in input().split(', ')]


total_pizza_made = 0
while pizza_orders and employees:
    cur_pizza = pizza_orders[0]
    cur_employee = employees[-1]
    max_order = 10
    if cur_pizza > max_order:
        pizza_orders.popleft()
        continue

    if cur_pizza <= 0:
        pizza_orders.popleft()
        continue

    if cur_pizza <= cur_employee:
        pizza_orders.popleft()
        employees.pop()
        total_pizza_made += cur_pizza
    else:

        pizza_orders[0] -= cur_employee
        total_pizza_made += cur_employee
        employees.pop()


if not pizza_orders:
    print(f'All orders are successfully completed!\n'
          f'Total pizzas made: {total_pizza_made}\n'
          f'Employees: {", ".join(str(x) for x in employees)}')
else:
    print(f'Not all orders are completed.\n'
         f'Orders left: {", ".join(str(x) for x in pizza_orders)}')


