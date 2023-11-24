import unittest
from Test import TestCalculator

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestCalculator('test_addition'))
    test_suite.addTest(TestCalculator('test_subtraction'))
    test_suite.addTest(TestCalculator('test_multiplication'))
    test_suite.addTest(TestCalculator('test_division'))
    test_suite.addTest(TestCalculator('test_division_by_zero'))
    return test_suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())