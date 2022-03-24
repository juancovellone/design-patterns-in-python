import unittest

from strategy.strategy import Calculator


class CalculatorTest(unittest.TestCase):

    def test_1_sum_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.calculate_operation('sum', 15, 5), 20)

    def test_2_subtraction_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.calculate_operation('subtraction', 15, 5), 10)

    def test_3_multiplication_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.calculate_operation('multiplication', 15, 5), 75)

    def test_4_division_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.calculate_operation('division', 15, 5), 3)

