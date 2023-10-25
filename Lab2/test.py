import unittest
from calculator import equal, window


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(int(equal("3+2")), 5)
    #     Тест суммы

    def test_subtract(self):
        self.assertEqual(int(equal("8-3")), 5)
    #     Тест вычитания

    def test_multiply(self):
        self.assertEqual(int(equal("10*2")), 20)
    #     Тест умножения

    def test_divide(self):
        self.assertEqual(float(equal("9/3")), 3.0)
    #     Тест деления
