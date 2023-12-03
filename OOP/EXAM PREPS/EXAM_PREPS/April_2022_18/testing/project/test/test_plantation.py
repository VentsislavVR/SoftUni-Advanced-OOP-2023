from unittest import TestCase

from plantation import Plantation


class PlantationTest(TestCase):
    def setUp(self):
        self.plantation = Plantation(2)

    def test_constructor(self):
        self.assertEqual(self.plantation.size, 2)
        self.assertEqual(self.plantation.plants, {})
        self.assertEqual(self.plantation.workers, [])

    def test_invalid_size_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            Plantation(-1)
        self.assertEqual("Size must be positive number!", str(ve.exception))

    def test_hire_worker_successfully(self):
        self.assertEqual([], self.plantation.workers)
        res = self.plantation.hire_worker('Gosho')
        self.assertEqual(['Gosho'], self.plantation.workers)
        self.assertEqual(res, "Gosho successfully hired.")

    def test_hire_worker_unsuccessfully_raises_value_error(self):
        self.assertEqual([], self.plantation.workers)

        self.plantation.hire_worker('Ivan')
        self.assertEqual(['Ivan'], self.plantation.workers)
        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker('Ivan')
        self.assertEqual("Worker already hired!", str(ve.exception))

        self.assertEqual(1, len(self.plantation.workers))

    def test_len_property(self):
        self.assertEqual(0, len(self.plantation.plants))

    def test_len_adding_plants(self):
        self.plantation.size = 3
        self.plantation.hire_worker('Test')
        self.plantation.planting('Test','Rose')

        self.assertEqual(1, len(self.plantation))
        self.plantation.planting('Test','Rose2')
        self.assertEqual(2, len(self.plantation))

        self.plantation.hire_worker('Test2')
        self.plantation.planting('Test2', 'Apple')

        self.assertEqual(3, len(self.plantation))

        self.assertEqual({"Test":['Rose','Rose2'],'Test2':['Apple']},
                         self.plantation.plants

                         )

    def test_planting_working_does_note_exist(self):
        self.plantation.hire_worker('Test')

        with self.assertRaises(ValueError) as ve:
            self.plantation.planting('Tester', 'Rose')
        self.assertEqual("Worker with name Tester is not hired!", str(ve.exception))

    def test_plantation_capacity_full_raises_value_error(self):
        self.plantation.hire_worker('Tester')
        self.plantation.planting('Tester', 'Rose')
        self.plantation.planting('Tester', 'Rose2')

        with self.assertRaises(ValueError) as ve:
            self.plantation.planting('Tester', 'Rose3')
        self.assertEqual("The plantation is full!", str(ve.exception))

    def test_plantation_adding_plants(self):
        self.plantation.hire_worker('Tester')
        res1 = self.plantation.planting('Tester', 'Rose')
        self.assertEqual(1, len(self.plantation))
        self.assertEqual("Tester planted it's first Rose.", res1)

        res2 = self.plantation.planting('Tester', 'Rose2')
        self.assertEqual(2, len(self.plantation))
        self.assertEqual("Tester planted Rose2.", res2)

    def test_str_(self):
        self.plantation.size = 3
        self.plantation.hire_worker('Test')
        self.plantation.hire_worker('Test2')

        self.plantation.planting('Test','Rose')
        self.plantation.planting('Test','Rose2')
        self.plantation.planting('Test2', 'Rose3')

        result = str(self.plantation)

        expected_value = "Plantation size: 3\nTest, Test2\nTest planted: Rose, Rose2\nTest2 planted: Rose3"

        self.assertEqual(expected_value,result)

    def test_repr(self):
        self.plantation.hire_worker('TEST')
        self.plantation.hire_worker('TEST2')

        result = repr(self.plantation)
        expected = f"Size: 2\n""Workers: TEST, TEST2"

        self.assertEqual(expected,result)

if __name__ == '__main__':
    ...
