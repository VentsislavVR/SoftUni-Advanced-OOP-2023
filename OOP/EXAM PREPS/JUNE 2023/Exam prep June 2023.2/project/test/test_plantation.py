from project.plantation import Plantation
from unittest import TestCase, main


class PlantationTest(TestCase):
    def setUp(self) -> None:
        self.plantation = Plantation(2)

    def test_constructor(self):
        self.assertEqual(2, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_size_is_negative_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.size = -5
        self.assertEqual("Size must be positive number!",
                         str(ve.exception))

    def test_hire_worker_that_exist_raises(self):
        self.plantation.hire_worker("Toni")
        self.assertEqual(["Toni"], self.plantation.workers)
        self.assertEqual(1, len(self.plantation.workers))
        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker("Toni")

        self.assertEqual("Worker already hired!",
                         str(ve.exception))
        self.assertEqual(["Toni"], self.plantation.workers)
        self.assertEqual(1, len(self.plantation.workers))

    def test_hire_new_worker(self):
        result = self.plantation.hire_worker("Johny")
        self.assertEqual(f"Johny successfully hired.",
                         result)

    def test_counting_plants__len__testing(self):
        self.plantation.plants["Plant"] = "plant"
        self.assertEqual(1, len(self.plantation.plants.items()))

    def test_planting_plants_no_worker_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Toni", "green")
        self.assertEqual(f"Worker with name Toni is not hired!",
                         str(ve.exception))
    def test_self_len(self):
        self.plantation.size = 3
        self.plantation.hire_worker("Toni")
        self.plantation.planting("Toni","green")
        self.assertEqual(1,len(self.plantation))

        self.plantation.planting("Toni", "green2")

        self.assertEqual(2, len(self.plantation))

        self.plantation.hire_worker("Johny")
        self.plantation.planting("Johny", "green3")

        self.assertEqual({"Toni":["green", "green2"],"Johny":["green3"]},
                        self.plantation.plants )
        self.assertEqual(3,len(self.plantation))

    def test_some_len_bigger_than_size_raises(self):
        self.plantation.size = 1
        self.plantation.hire_worker("Toni")
        self.plantation.hire_worker("Toni2")

        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Toni", "green")
            self.plantation.planting("Toni2", "green")
        self.assertEqual("The plantation is full!",
                         str(ve.exception))

    def test_planting_first_plant_for_worker(self):
        self.plantation.hire_worker("Toni")
        result = self.plantation.planting("Toni", "green")
        self.assertEqual({"Toni": ["green"]}, self.plantation.plants)
        self.assertEqual("Toni planted it's first green.",
                         result)

    def test_planting_more_plants_for_worker(self):
        self.plantation.hire_worker("Toni")
        self.plantation.planting("Toni", "green")
        self.assertEqual({"Toni":["green"]},self.plantation.plants)
        result = self.plantation.planting("Toni", "other green")
        self.assertEqual(f"Toni planted other green.",
                         result)
        self.assertEqual(2,len(self.plantation.plants["Toni"]))

    def test_str_method(self):
        self.plantation.size = 1
        self.plantation.workers = ["Toni"]
        self.plantation.plants["Toni"] = ["green"]

        expected = ("Plantation size: 1\n"
                    "Toni\n"
                    "Toni planted: green")
        self.assertEqual(expected, str(self.plantation))

    def test__repr_method(self):
        self.plantation.size = 1
        self.plantation.workers = ["Toni"]

        expected = "Size: 1\nWorkers: Toni"
        self.assertEqual(expected, repr(self.plantation))


if __name__ == "__main__":
    main()
