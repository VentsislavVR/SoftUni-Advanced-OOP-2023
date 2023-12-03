import unittest

from project.trip import Trip
from unittest import TestCase

class TestTrip(TestCase):
    def setUp(self):
        self.t1f = Trip(10_000,1,False)
        self.t2f = Trip(10_000,2,False)
        self.t2t = Trip(10_000,2,True)
    def test_initialization_trip(self):
        self.assertEqual(10_000,self.t2t.budget)
        self.assertEqual(2,self.t2t.travelers)
        self.assertFalse(self.t2f.is_family)
        self.assertEqual({},self.t2f.booked_destinations_paid_amounts)

    def test_setter_travelers(self):
        with self.assertRaises(ValueError) as ex:
            self.t1f.travelers = 0
        self.assertEqual("At least one traveler is required!", str(ex.exception))

    def test_setter_is_family(self):
        self.assertTrue(self.t2t.is_family)

        self.t1f.is_family = True

        self.assertFalse(self.t1f.is_family)

    def test_book_a_trip_not_in_offer(self):
        self.assertEqual("This destination is not in our offers, please choose a new one!",
                         self.t2t.book_a_trip('asd'))
    def test_book_a_trip_not_enough_budget(self):
        test = self.t2t.book_a_trip('New Zealand')
        self.assertEqual('Your budget is not enough!',test)

    def test_book_trip_successfully_no_family_discount(self):
        self.assertEqual(self.t2f.book_a_trip('Bulgaria'),
                         f'Successfully booked destination Bulgaria! Your budget left is 9000.00')
        self.assertEqual(self.t2f.budget,9000)
        self.assertEqual(self.t2f.booked_destinations_paid_amounts,{'Bulgaria':1000})
    def test_book_trip_successfully_with_discount(self):
        self.assertEqual(self.t2t.book_a_trip('Bulgaria'),
                         f'Successfully booked destination Bulgaria! Your budget left is 9100.00')
        self.assertEqual(self.t2t.budget,9100 )
        self.assertEqual(self.t2t.booked_destinations_paid_amounts,{'Bulgaria':900})

    def test_booking_status_no_bookings(self):
        self.assertEqual(self.t2t.booking_status(),
                         f'No bookings yet. Budget: 10000.00')
    def test_booking_status_with_bookings(self):
        self.t2t.book_a_trip('Bulgaria')
        self.assertEqual(self.t2t.booking_status(),
                         ("Booked Destination: Bulgaria\n"
                          "Paid Amount: 900.00\n"
                          "Number of Travelers: 2\n"
                          "Budget Left: 9100.00"))


if __name__ == '__main__':
    unittest.main()






