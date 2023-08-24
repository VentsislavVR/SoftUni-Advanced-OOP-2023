from project.shopping_cart import ShoppingCart

from unittest import TestCase,main

class TestShoppingCart(TestCase):

    def setUp(self) -> None:
        self.cart = ShoppingCart('Test',100)
    def test_proper_initialization(self):
        self.assertEqual('Test',self.cart.shop_name)
        self.assertEqual(100,self.cart.budget)
        self.assertEqual({},self.cart.products)

    def test_invalid_shop_name_lowwer_first_raises(self):
        with self.assertRaises(ValueError) as ve:
            ShoppingCart('test', 100)
        self.assertEqual("Shop must contain only letters and must start with capital letter!",
                         str(ve.exception))
    def test_invalid_shop_name_not_is_all_alpha_first_raises(self):
        with self.assertRaises(ValueError) as ve:
            ShoppingCart('Tes1', 100)
        self.assertEqual("Shop must contain only letters and must start with capital letter!",
                         str(ve.exception))
    def test_add_to_cart_too_expensive_product_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.add_to_cart('meat',150)
        self.assertEqual("Product meat cost too much!",
                         str(ve.exception))
    def test_add_item_to_cart(self):
        result = self.cart.add_to_cart('meat',15)
        self.assertEqual(f"meat product was successfully added to the cart!",
                         result)
        self.assertEqual(1,len(self.cart.products))
        self.assertEqual({'meat':15},self.cart.products)

    def test_remove_item_that_does_not_exist_raises(self):
        self.assertEqual(0,len(self.cart.products))
        with self.assertRaises(ValueError) as ve:
            self.cart.remove_from_cart('meat')
        self.assertEqual("No product with name meat in the cart!",
                                   str(ve.exception))
    def test_remove_item_successfully(self):
        self.cart.add_to_cart('meat',15)
        self.assertEqual(1, len(self.cart.products))

        result = self.cart.remove_from_cart('meat')
        self.assertEqual('Product meat was successfully removed from the cart!',result)
        self.assertEqual(0,len(self.cart.products))

    def test__add__shopping_carts_names(self):
        other = ShoppingCart('Testt',100)
        new = self.cart.__add__(other)
        self.assertEqual('TestTestt',new.shop_name)

    def test__add__shopping_carts_budget(self):
        other = ShoppingCart('Testt',100)
        new = self.cart.__add__(other)
        self.assertEqual(200,new.budget)

    def test__add__shopping_carts_new_priducts(self):
        self.cart.add_to_cart('meat',20)
        other = ShoppingCart('Testt',100)
        other.add_to_cart('more meat',99)

        new = self.cart.__add__(other)

        self.assertEqual(2,len(new.products))
        self.assertEqual({'meat':20,'more meat':99},new.products)
    def test_adding_kwargs(self):
        self.cart.add_to_cart('meat', 20)
        other = ShoppingCart('Testt', 100)
        other.add_to_cart('more meat', 99,)
        other.add_to_cart('eggs', 20, )

        new = self.cart.__add__(other)

        self.assertEqual(3, len(new.products))
        self.assertEqual({'meat': 20, 'more meat': 99,'eggs':20}, new.products)
    def test_new_shopping_object(self):
        other = ShoppingCart('Testt', 100)
        new = self.cart.__add__(other)
        self.assertEqual(new.products,self.cart.__add__(other).products)
    def test_buy_products_with_insufficient_budget(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.add_to_cart('meat',80)
            self.cart.add_to_cart('eggs',25)
            self.cart.buy_products()
        self.assertEqual("Not enough money to buy the products! Over budget with"
                         " 5.00lv!",str(ve.exception))
    def test_buy_products(self):
        self.cart.add_to_cart('meat',99)
        result = self.cart.buy_products()
        self.assertEqual('Products were successfully bought! Total cost: 99.00lv.',
                         result)


if __name__ == '__main__':
    main()