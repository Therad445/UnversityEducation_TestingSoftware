import unittest
from controller import Controller

class TestController(unittest.TestCase):
    def setUp(self):
        self.controller = Controller()

    def test_on_button_click(self):
        # Test addition
        self.controller.on_button_click(1)
        self.controller.on_button_click('+')
        self.controller.on_button_click(2)
        self.assertEqual(self.controller.view.value_var.get(), '3.0')

        # Test subtraction
        self.controller.on_button_click(5)
        self.controller.on_button_click('-')
        self.controller.on_button_click(3)
        self.assertEqual(self.controller.view.value_var.get(), '2.0')

        # Test multiplication
        self.controller.on_button_click(4)
        self.controller.on_button_click('*')
        self.controller.on_button_click(3)
        self.assertEqual(self.controller.view.value_var.get(), '12.0')

        # Test division
        self.controller.on_button_click(9)
        self.controller.on_button_click('/')
        self.controller.on_button_click(3)
        self.assertEqual(self.controller.view.value_var.get(), '3.0')

    def test_clear(self):
        self.controller.on_button_click(1)
        self.controller.on_button_click('C')
        self.assertEqual(self.controller.view.value_var.get(), '')

    def test_change_type(self):
        self.controller.on_button_click(1)
        self.controller.on_button_click('+/-')
        self.assertEqual(self.controller.view.value_var.get(), '-1')

    def test_percentage(self):
        self.controller.on_button_click(5)
        self.controller.on_button_click(0)
        self.controller.on_button_click('%')
        self.assertEqual(self.controller.view.value_var.get(), '0.5')

    def test_decimal(self):
        self.controller.on_button_click(1)
        self.controller.on_button_click('.')
        self.controller.on_button_click(5)
        self.assertEqual(self.controller.view.value_var.get(), '1.5')

if __name__ == '__main__':
    unittest.main()