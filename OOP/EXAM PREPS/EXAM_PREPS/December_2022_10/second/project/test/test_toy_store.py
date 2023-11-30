from unittest import TestCase,main

from project.toy_store import ToyStore

class TestToyStore(TestCase):

    def setUp(self):
        self.store = ToyStore()
    def test_correct_init(self):
        for key in range(ord('A'),ord('G')+1):
            self.assertIsNone(self.store.toy_shelf[chr(key)])

    def test_add_toy_non_existing_toy_shelf_raises_exception(self):
        with self.assertRaises(Exception) as ve:
            self.store.add_toy('Z', 'Teddy')
        self.assertEqual("Shelf doesn't exist!",str(ve.exception))

    def test_add_toy_toy_in_shelf_raise_exception(self):
        self.store.add_toy('A', 'Teddy')
        with self.assertRaises(Exception) as ve:
            self.store.add_toy('A', 'Teddy')
        self.assertEqual("Toy is already in shelf!",str(ve.exception))

    def test_add_toy_on_taken_shelf_raise_exception(self):
        self.store.add_toy('A', 'Teddy')
        with self.assertRaises(Exception) as ve:
            self.store.add_toy('A', 'Car')
        self.assertEqual("Shelf is already taken!", str(ve.exception))

    def test_add_toy(self):
        res = self.store.add_toy('A', 'Teddy')
        self.assertEqual(f"Toy:Teddy placed successfully!", res)


    def test_remove_toy_not_existing_shelf(self):
        with self.assertRaises(Exception) as ve:
            self.store.remove_toy('Z', 'Teddy')
        self.assertEqual("Shelf doesn't exist!",str(ve.exception))


    def test_toy_in_shelf(self):
        self.store.add_toy('A', 'Teddy')
        with self.assertRaises(Exception) as ve:
            self.store.remove_toy('A', 'Teddy2')
        self.assertEqual("Toy in that shelf doesn't exists!", str(ve.exception))
    def test_remove_toy_(self):
        self.store.add_toy('A', 'Teddy')
        self.assertEqual(self.store.toy_shelf['A'],'Teddy')

        res = self.store.remove_toy('A', 'Teddy')
        self.assertEqual(self.store.toy_shelf['A'],None)
        self.assertEqual(f"Remove toy:Teddy successfully!",res)



if __name__ == '__main__':
    main()