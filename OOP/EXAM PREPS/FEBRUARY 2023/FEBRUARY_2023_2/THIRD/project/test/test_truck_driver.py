from project.truck_driver import TruckDriver

from unittest import TestCase, main


class TestTruckDriver(TestCase):
    def setUp(self) -> None:
        self.driver = TruckDriver("Test", 1)

    def test_init(self):
        driver = TruckDriver("Test", 1)
        self.assertEqual("Test", self.driver.name)
        self.assertEqual(1, self.driver.money_per_mile)
        self.assertEqual({}, self.driver.available_cargos)
        self.assertEqual(0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)

    def test_earned_money_negative_value_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.driver.earned_money = -1
            self.assertEqual(f"{self.name} went bankrupt."
                             , str(ve.exception))

    def test_earned_money_positive_value(self):
        self.driver.earned_money += 5
        self.assertEqual(5, self.driver.earned_money)

    def test_add_existing_cargo_raises(self):
        self.driver.available_cargos["Varna"] = 5

        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer("Varna"
                                        , 5)

        self.assertEqual("Cargo offer is already added.",
                         str(ex.exception))

    def test_add_cargo_successfully(self):
        result = self.driver.add_cargo_offer("Varna", 5)
        self.assertEqual(f"Cargo for 5 "
                         f"to Varna "
                         f"was added as an offer.",
                         result
                         )

    def test_drive_best_cargo_offer_no_offer_raises(self):

            self.driver.available_cargos = {}
            res = self.driver.drive_best_cargo_offer()

            self.assertEqual("There are no offers available.", res)

    def test_drive_cargo_offer(self):
        self.driver.add_cargo_offer("Varna", 100)
        self.driver.add_cargo_offer("Sofia", 200)
        self.driver.add_cargo_offer("Burgas", 300)

        self.assertEqual(3, len(self.driver.available_cargos))

        result = self.driver.drive_best_cargo_offer()
        self.assertEqual(f"Test is driving 300 to Burgas."
                         , result)
        self.assertEqual(280, self.driver.earned_money)
        self.assertEqual(300, self.driver.miles)

    def test_eat(self):
        self.driver.earned_money = 50
        self.driver.eat(250)

        self.assertEqual(30, self.driver.earned_money)

    def test_sleep(self):
        self.driver.earned_money = 50
        self.driver.sleep(1000)

        self.assertEqual(5, self.driver.earned_money)

    def test_pump(self):
        self.driver.earned_money = 600
        self.driver.pump_gas(1500)
        self.assertEqual(100, self.driver.earned_money)

    def test_repair(self):
        self.driver.earned_money = 7600
        self.driver.repair_truck(10000)
        self.assertEqual(100, self.driver.earned_money)

    def test__repr__(self):
        self.driver.miles = 50
        res = str(self.driver)
        self.assertEqual(f"Test "
                         f"has 50 "
                         f"miles behind his back.", res)


if __name__ == '__main__':
    main()
