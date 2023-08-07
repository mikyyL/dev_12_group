import unittest


class Calculator:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_sum(self):
        return self.x + self.y

    def get_diff(self):
        return self.x - self.y


class TestCalculator(unittest.TestCase):

    def test_sum(self):
        calculator = Calculator(8, 2)
        self.assertEqual(calculator.get_sum(), 10, 'The sum is wrong')

    def test_diff(self):
        calculator = Calculator(8, 2)
        self.assertEqual(calculator.get_diff(), 6, 'The differance is wrong')
