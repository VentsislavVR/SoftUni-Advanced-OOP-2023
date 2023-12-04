from unittest import TestCase

from project.second_hand_car import SecondHandCar
class TestSecondHandCar(TestCase):
    def setUp(self):
        self.car = SecondHandCar('Model','type',100_000,1000)

    def test_init(self):
        self.assertEqual(self.car.model, 'Model')
        self.assertEqual(self.car.car_type,'type')
        self.assertEqual(self.car.mileage,100_000)
        self.assertEqual(self.car.price,1000)

    def test_price_lt_1_raises_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.car.price = 0.5
        expected_message = 'Price should be greater than 1.0!'
        self.assertEqual(expected_message, str(ve.exception))

    def test_mileage_lte_100_raises_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 99
        expected_message = 'Please, second-hand cars only! Mileage must be greater than 100!'
        self.assertEqual(expected_message, str(ve.exception))

    def test_set_promotional_price_old_gte_new_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(1500)
        expected_message = 'You are supposed to decrease the price!'
        self.assertEqual(expected_message,str(ve.exception))

    def test_promotional_price_success(self):
        res = self.car.set_promotional_price(999)
        self.assertEqual('The promotional price has been successfully set.',res)
        self.assertEqual(999,self.car.price)

    def test_repair_too_expensive(self):
        res =self.car.need_repair(600,'Broken')
        self.assertEqual('Repair is impossible!',res)
    def test_repairing_car(self):
        self.assertEqual([],self.car.repairs)
        res = self.car.need_repair(200,'less broken')
        self.assertEqual(f'Price has been increased due to repair charges.',res)
        self.assertEqual(1200,self.car.price)
        self.assertEqual(['less broken'],self.car.repairs)

    def test_gt_missmatch(self):
        self.car2 = SecondHandCar('Model2', 'type2',1000,1500)
        res = self.car.__gt__(self.car2)
        self.assertEqual('Cars cannot be compared. Type mismatch!',res)
    def test_proper_comparison(self):
        self.car2 = SecondHandCar('Model2', 'type',1000,1500)
        self.assertEqual(self.car.__gt__(self.car2),False)

        self.car3 = SecondHandCar('Model3', 'type', 1000, 500)
        self.assertEqual(self.car.__gt__(self.car3), True)
    def test_str(self):
            self.assertEqual("Model Model | Type type | Milage 100000km\nCurrent price: 1000.00 | Number of Repairs: 0",str(self.car))
