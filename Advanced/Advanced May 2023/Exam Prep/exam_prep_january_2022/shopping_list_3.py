def shopping_list(budget,**kwargs):
    result = []
    basket = {}
    if budget < 100:
        return f'You do not have enough budget.'
    for product_name,quantity in kwargs.items():
        current_cost = quantity[0] * quantity[1]
        if current_cost > budget:
            continue
        if len(basket) >=5 or not kwargs:
             break

        if product_name not in basket:
                basket[product_name] = current_cost
                if basket[product_name] > budget:
                    break
                budget -= basket[product_name]
        else:
            basket[product_name] += current_cost
            budget -= basket[product_name]
    for pr , price in basket.items():
        result.append(f"You bought {pr} for {price:.2f} leva.")
    return '\n'.join(result)
# def shopping_list(budget, **kwargs):
#     result = []
#     basket = set()
#
#     if budget < 100:
#         return 'You do not have enough budget.'
#
#     for product_name, quantity in kwargs.items():
#         current_cost = quantity[0] * quantity[1]
#
#         if current_cost > budget:
#             continue
#
#         if len(basket) >= 5 or not kwargs:
#             break
#
#         if product_name not in basket:
#             basket.add(product_name)
#             budget -= current_cost
#
#     for product in basket:
#         result.append(f"You bought {product} for {kwargs[product][0] * kwargs[product][1]:.2f} leva.")
#
#     return '\n'.join(result)


print(shopping_list(104,
cola=(1.20, 2),
candies=(0.25, 15),
bread=(1.80, 1),
pie=(10.50, 5),
tomatoes=(4.20, 1),
milk=(2.50, 2),
juice=(2, 3),
eggs=(3, 1),
))
print("&" * 50)
print(shopping_list(100,

microwave=(70, 2),

skirts=(15, 4),
coffee=(1.50, 10), ))

import unittest

class Tests(unittest.TestCase):
    def test(self):
        result = shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    )
        self.assertEqual(result.strip(), "You bought skirts for 60.00 leva.\nYou bought coffee for 15.00 leva.")

if __name__ == "__main__":
    unittest.main()