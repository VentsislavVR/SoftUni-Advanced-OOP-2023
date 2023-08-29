def flights(*args):
    total_flights = {}

    for current in range(0,len(args),2):
        if args[current] == 'Finish':
            break

        if args[current] not in total_flights:
            total_flights[args[current]] = 0
        total_flights[args[current]] += args[current+1]

    return total_flights


print(flights('Vienna', 256, 'Vienna', 26,

              'Morocco', 98, 'Paris', 115, 'Finish',

              'Paris', 15))


print(flights('London', 0, 'New York', 9,

'Aberdeen', 215, 'Sydney', 2, 'New York',

300, 'Nice', 0, 'Finish'))

# import unittest
#
# class Tests(unittest.TestCase):
#     def test(self):
#         result = flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15)
#         self.assertEqual(result, {'Vienna': 282, 'Morocco': 98, 'Paris': 115})
#
# if __name__ == "__main__":
#     unittest.main()
