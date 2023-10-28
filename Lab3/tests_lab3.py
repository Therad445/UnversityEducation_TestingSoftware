import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_button_press(self):
        for button in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '+', '-', '*', '/', '=', 'Clear', 'Close']:
            self.calculator.button_press(button)
            self.assertEqual(self.calculator.entry.get(), button)

    def test_equal_button(self):
        self.calculator.button_press('1')
        self.calculator.button_press('2')
        self.calculator.button_press('=')
        self.assertEqual(self.calculator.entry.get(), '3')

    def test_clear_button(self):
        self.calculator.button_press('1')
        self.calculator.button_press('2')
        self.calculator.button_press('Clear')
        self.assertEqual(self.calculator.entry.get(), '')

    def test_close_button(self):
        self.calculator.button_press('1')
        self.calculator.button_press('2')
        self.calculator.button_press('Close')
        self.assertEqual(self.calculator.entry.get(), '')
        self.assertFalse(self.calculator.window.winfo_exists())

if __name__ == '__main__':
    unittest.main()
