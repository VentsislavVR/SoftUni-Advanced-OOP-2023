from project.pet_shop import PetShop
from unittest import TestCase,main


class TestPetShop(TestCase):
    def setUp(self) -> None:
        self.pet_shop = PetShop('PetShop')
    def proper_initialization(self):

        name = 'PetShop'
        pet_shop = PetShop('PetShop')

        self.assertEqual(name,pet_shop.name)
        self.assertEqual({},pet_shop.food)
        self.assertEqual([],pet_shop.pets)


    def test_add_food_raises_when_negative_or_0(self):
        with self.assertRaises(ValueError) as context:
            self.pet_shop.add_food('Pesho',-25)
        self.assertEqual("Quantity cannot be equal to or less than 0",
                          str(context.exception))
    def test_add_food(self):
        self.pet_shop.add_food('pesho',25)
        self.assertEqual({'pesho':25},self.pet_shop.food)
        res = self.pet_shop.add_food('pesho',25)
        self.assertEqual(f"Successfully added 25.00 grams of pesho."
                          ,res)

    def test_add_pet_raises(self):
        with self.assertRaises(Exception) as ex:
            self.pet_shop.add_pet('ariel')
            self.pet_shop.add_pet('ariel')
        self.assertEqual("Cannot add a pet with the same name",
                         str(ex.exception))
    def test_add_pet(self):
        res = self.pet_shop.add_pet('ariel')
        self.assertEqual('Successfully added ariel.',
                         res)
    def test_feed_pet_invalid_pet_raises(self):
        with self.assertRaises(Exception) as ex:
            self.pet_shop.feed_pet('gosho','gosho')
        self.assertEqual(f"Please insert a valid pet name",
                         str(ex.exception))
    def test_feed_pet_invalid_food_name(self):
        self.pet_shop.add_pet('ariel')
        res = self.pet_shop.feed_pet('gosho','ariel')
        self.assertEqual(f'You do not have gosho',
                         res)
    def test_adding_food_below_100(self):
        self.pet_shop.add_pet('ariel')
        self.pet_shop.add_food('gosho',50)
        res = self.pet_shop.feed_pet('gosho','ariel')
        self.assertEqual('Adding food...',
                         res)
        self.assertEqual(self.pet_shop.food,
                         {'gosho':1050})
        res=self.pet_shop.feed_pet('gosho','ariel')
        self.assertEqual(f"ariel was successfully fed",
                         res)
        self.assertEqual(950,self.pet_shop.food['gosho'])

    def test__repr__(self):
        self.pet_shop.add_pet('ariel')
        self.pet_shop.add_pet('ARIEL')
        exp = f'Shop PetShop:\n' \
               f'Pets: ariel, ARIEL'

        res = self.pet_shop.__repr__()
        self.assertEqual(exp,res)


if __name__ == '__main__':
    main()