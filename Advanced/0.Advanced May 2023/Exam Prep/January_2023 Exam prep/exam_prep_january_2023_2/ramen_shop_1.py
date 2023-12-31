from collections import deque


bowls_of_ramen= [int(x)for x in input().split(", ")]
customers = deque(int(x) for x in input().split(","))


while bowls_of_ramen and customers:
    ramen = bowls_of_ramen.pop()
    customer = customers.popleft()

    if ramen == customer:
        continue

    elif ramen > customer:
        bowls_of_ramen.append(ramen - customer)

    elif customer > ramen:
        customers.appendleft(customer - ramen)

if not customers:
    print(f"Great job! You served all the customers.")
    if bowls_of_ramen:
        print(f"Bowls of ramen left: {', '.join(str(x) for x in bowls_of_ramen)}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    if customers:
        print(f"Customers left: {', '.join(str(x) for x in customers)}")




