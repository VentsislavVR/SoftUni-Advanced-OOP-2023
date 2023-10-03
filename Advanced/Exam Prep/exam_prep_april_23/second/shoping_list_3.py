# def shop_from_grocery_list(budget, grocery_list,*args):
#     purchased_items = set()
#     result = []
#     for item in args:
#         if item[0] in purchased_items:
#             continue
#         if item[0] not in grocery_list:
#             continue
#         if budget - item[1] >=0:
#             purchased_items.add(item[0])
#             budget -= item[1]
#         else:
#             break
#     if purchased_items.issubset(grocery_list) and len(purchased_items) == len(grocery_list):
#             result.append(f"Shopping is successful. Remaining budget: {budget:.2f}.")
#     else:
#         result.append(f"You did not buy all the products. Missing products: ")
#         for item in purchased_items:
#             result.append(f"{', '.join(purchased_items.symmetric_difference(grocery_list))}.")
#             break
#     return ''.join(result)

def shop_from_grocery_list(budget, grocery_list, *args):
    purchased_items = set()

    for item in args:
        item_name, item_price = item[0], item[1]

        if item_name in purchased_items:
            continue

        if item_name not in grocery_list:
            continue

        if budget - item_price >= 0:
            purchased_items.add(item_name)
            budget -= item_price
        else:
            break

    if purchased_items == set(grocery_list):
        result = f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        missing_items = set(grocery_list) - purchased_items
        result = "You did not buy all the products. Missing products: "
        result += ', '.join(missing_items) + '.'

    return result


from unittest import TestCase, main

class Test(TestCase):
    def test_students_credits(self):
        result = shop_from_grocery_list(
            100,
            ["tomato", "cola", "chips", "meat"],
            ("cola", 5.8),
            ("tomato", 10.0),
            ("meat", 22))

        self.assertEqual(
            result.strip(),
            """You did not buy all the products. Missing products: chips.""")

if __name__ == '__main__':
    main()