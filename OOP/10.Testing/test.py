from unittest import TestCase, main
from car_manager import Car


class CarTest(TestCase):
    def setUp(self):
        self.car = Car("Nissan", "GT-R", 15, 75)

    def test_correct_innit(self):
        self.assertEqual("Nissan", self.car.make)
        self.assertEqual("GT-R", self.car.model)
        self.assertEqual(15, self.car.fuel_consumption)
        self.assertEqual(75, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_with_null_or_empty_value_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""
        self.assertEqual("Make cannot be null or empty!",
                         str(ex.exception))

    def test_model_with_empty_value_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""
        self.assertEqual("Model cannot be null or empty!",
                         str(ex.exception))
    def test_fuel_conumption_negative_value_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -1
        self.assertEqual("Fuel consumption "
                         "cannot be zero or negative!",
                         str(ex.exception))

    def test_fuel_capacity_with_negative_value_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -1
        self.assertEqual("Fuel capacity cannot be zero or negative!",
                         str(ex.exception))

    def test_fuel_amount_with_negative_value_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!"
                         ,str(ex.exception))

    def test_refuel_with_negative_amount_or_zero(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-1)
        self.assertEqual("Fuel amount cannot be zero or negative!"
                         ,str(ex.exception))

    def test_refuel_with_positive_valid_value(self):
        self.car.refuel(10)
        self.assertEqual(10,self.car.fuel_amount)

    def test_refuel_with_excess_amount(self):
        self.car.refuel(85)
        self.assertEqual(75,self.car.fuel_amount)

    def test_drive_with_insufficient_fuel_amount(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(1000)
        self.assertEqual("You don't have enough fuel to drive!",
                         str(ex.exception))
    def test_driving_with_sufficient_fuel(self):
        self.car.fuel_amount = 30
        self.car.drive(100)
        self.assertEqual(15,self.car.fuel_amount)

if __name__ == "__main__":
    main()
