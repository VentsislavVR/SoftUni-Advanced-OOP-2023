import unittest
from collections import deque

from project.railway_station import RailwayStation

import unittest


class TestRailwayStation(unittest.TestCase):
    def setUp(self):
        self.station = RailwayStation("TestStation")

    def test_station_name_length(self):
        with self.assertRaises(ValueError) as ve:
            RailwayStation("AB")
        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_proper_init_with_longer_name(self):
        station = RailwayStation("LongStationName")
        self.assertEqual(station.name, "LongStationName")
        self.assertEqual(station.arrival_trains, deque())
        self.assertEqual(station.departure_trains, deque())

    def test_empty_station_status(self):
        self.assertEqual(len(self.station.arrival_trains), 0)
        self.assertEqual(len(self.station.departure_trains), 0)

    def test_new_arrival_on_board(self):
        self.station.new_arrival_on_board("Train1")
        self.assertEqual(self.station.arrival_trains, deque(["Train1"]))

    def test_train_has_arrived(self):
        self.station.new_arrival_on_board("Train1")
        result = self.station.train_has_arrived("Train1")
        self.assertEqual(result, "Train1 is on the platform and will leave in 5 minutes.")
        self.assertEqual(self.station.arrival_trains, deque())
        self.assertEqual(self.station.departure_trains, deque(["Train1"]))
        self.assertEqual(len(self.station.arrival_trains), 0)
        self.assertEqual(len(self.station.departure_trains), 1)

    def test_train_has_arrived_with_other_trains(self):
        self.station.new_arrival_on_board("Train1")
        self.station.new_arrival_on_board("Train2")
        result = self.station.train_has_arrived("Train2")
        self.assertEqual(result, "There are other trains to arrive before Train2.")
        self.assertEqual(len(self.station.arrival_trains), 2)
        self.assertEqual(len(self.station.departure_trains), 0)

    def test_train_has_left(self):
        self.station.new_arrival_on_board("Train1")
        self.station.train_has_arrived("Train1")
        result = self.station.train_has_left("Train1")
        self.assertTrue(result)
        self.assertEqual(self.station.departure_trains, deque())
        self.assertEqual(len(self.station.departure_trains), 0)

    def test_train_has_left_wrong_train(self):
        self.station.new_arrival_on_board("Train1")
        self.station.train_has_arrived("Train1")
        result = self.station.train_has_left("Train2")
        self.assertFalse(result)
        self.assertEqual(self.station.departure_trains, deque(["Train1"]))


if __name__ == '__main__':
    unittest.main()
