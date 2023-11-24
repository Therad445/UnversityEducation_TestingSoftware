import unittest
from unittest.mock import patch
from io import StringIO
from calculator import main
import sys


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.output = StringIO()
        self.old_stdout = sys.stdout
        sys.stdout = self.output

    def tearDown(self):
        sys.stdout = self.old_stdout

    def test_addition(self):
        with patch('builtins.input', side_effect=['1', '+', '2', '=']):
            main()
        self.assertEqual(self.output.getvalue().strip(), '3')

    def test_subtraction(self):
        with patch('builtins.input', side_effect=['5', '-', '3', '=']):
            main()
        self.assertEqual(self.output.getvalue().strip(), '2')

    def test_multiplication(self):
        with patch('builtins.input', side_effect=['2', '*', '3', '=']):
            main()
        self.assertEqual(self.output.getvalue().strip(), '6')

    def test_division(self):
        with patch('builtins.input', side_effect=['6', '/', '3', '=']):
            main()
        self.assertEqual(self.output.getvalue().strip(), '2')

    def test_division_by_zero(self):
        with patch('builtins.input', side_effect=['6', '/', '0', '=']):
            main()
        self.assertIn('Error', self.output.getvalue())
