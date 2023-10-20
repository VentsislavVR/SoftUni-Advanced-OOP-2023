
def stock_availability(inventory, action, *args):
    if action == "delivery":
        inventory.extend(args)
    elif action == "sell":
        if not args:
            inventory.pop(0)  # Sell the first box
        else:
            if isinstance(args[0], int):
                num_to_sell = args[0]
                inventory = inventory[num_to_sell:]
            else:
                flavors_to_sell = set(args)
                inventory = [box for box in inventory if box not in flavors_to_sell]
    return inventory

print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
