import unittest
from calculator import add
from calculator import multiply
from calculator import divide

from calculator import subtract

class CustomException(BaseException):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2


class CalculatorTest(unittest.TestCase):
    def test_add(self):
        first_number = 2.8
        second_number = 4.1
        answer = add(first_number, second_number)
        self.assertEqual(answer, 6.9)
        assert type(answer) == float

    def test_multiply(self):
        first_number = -3
        second_number = 5
        answer = multiply(first_number, second_number)
        self.assertEqual(answer, -15)
        assert type(answer) == int

    def test_divide(self):
        self.assertEqual(divide(10,5), 2)
        self.assertEqual(divide(30,10), 3)
        self.assertEqual(divide(10,0), 0)





    # def test_divide(self):
    #     try:
    #         first_number = 13
    #         second_number = 0
    #         if first_number == 0 or second_number == 0:
    #             raise CustomException(first_number, second_number)
    #
    #         # answer = divide(first_number, second_number)
    #     # except ZeroDivisionError:
    #     #     print(f"Oopsie! You chose the numbers {first_number} and {second_number}. I'm sorry my love but you can't divide by zero")
    #     except CustomException as err:
    #         print(f"Oopsie! You chose the numbers {err.arg1} and {err.arg2}. I'm sorry my love but you can't divide by zero")




                # first_number = 1000
        # second_number = 0
        # self.assertRaises(ValueError, divide(first_number, second_number))
