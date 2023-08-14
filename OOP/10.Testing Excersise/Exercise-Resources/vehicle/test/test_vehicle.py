
from unittest import TestCase,main
from project.vehicle import Vehicle
class TestVehicle(TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(20.5,175.5)

    def test_default_fuel_consumption_class_attribute(self):

        self.assertEqual(1.25,Vehicle.DEFAULT_FUEL_CONSUMPTION)


    def test_correct_initializing(self):
        self.assertEqual(20.5, self.vehicle.fuel)
        self.assertEqual(20.5, self.vehicle.capacity)
        self.assertEqual(175.5, self.vehicle.horse_power)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION,self.vehicle.fuel_consumption)

    def test_vehicle_drives_without_fuel_raises(self):
        self.vehicle.fuel = 0
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)
        self.assertEqual("Not enough fuel",str(ex.exception))
    def test_vehicle_has_fuel_and_is_driving(self):
        self.vehicle.drive(2)
        self.assertEqual(18,self.vehicle.fuel)

    def test_refuel_vehicle_more_than_capacity(self):
        self.vehicle.fuel = 19.5
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(2)
        self.assertEqual("Too much fuel",str(ex.exception))

    def test_refueling_vehicle_successfully(self):
        self.vehicle.fuel = 15
        self.vehicle.refuel(5)
        self.assertEqual(20,self.vehicle.fuel)

    def test_correct__str__method(self):
        result = str(self.vehicle)
        expected = f"The vehicle has 175.5 " \
                f"horse power with 20.5 fuel left"\
                f" and 1.25 fuel"\
                f" consumption"
        self.assertEqual(result,expected)


if __name__ == "__main__":
    main()