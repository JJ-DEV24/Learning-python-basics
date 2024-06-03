import unittest

import Cars_class

Cars_class.main()

from Cars_class import Cars

from Cars_class import ElectricCars


class TestCars(unittest.TestCase):

    def setUp(self):
        self.jess_car = Cars('BMW', 'silver', 6)
        self.pedro_car = Cars('Ford', 'yellow', 2)

    def tearDown(self):
        pass

    def test_car_make(self):
        self.jess_car.make = 'Tesla'
        print('Test for make of car')
        self.assertEqual(self.jess_car.make, 'Tesla')
        self.assertEqual(self.pedro_car.make, 'Ford')

    def test_car_colour(self):
        self.pedro_car.colour = 'poo'
        print('Test for colour of car')
        self.assertEqual(self.jess_car.colour, 'silver')
        self.assertEqual(self.pedro_car.colour, 'poo')

    def test_car_doors(self):
        print('Test for number of car doors')
        self.assertEqual(self.jess_car.doors, 6)
        self.assertEqual(self.pedro_car.doors, 2)


# self.assertEqual(jess_car.make, 'Tesla')
# self.assertEqual(pedro_car.colour, 'poo')

# @classmethod
# def get_number_of_household_cars(cls):
#     return cls.total_cars_at_Sa_Dias_residence
# @classmethod
# def add_car(cls):
#     cls.total_cars_at_Sa_Dias_residence += 1
#
#     total_cars_at_Sa_Dias_residence: int = 0
#
#
# self.assertEqual(total_cars_at_Sa_Dias_residence, 4)
