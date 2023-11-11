import unittest
from unittest.mock import Mock, MagicMock
from controller import Controller


class TestView(unittest.TestCase):
    mock_button = MagicMock()

    def setUp(self):
        self.mock_view = Mock()
        self.mock_calculator = Mock()
        self.controller = Controller(self.mock_calculator, self.mock_view)

    def test_clear(self):
        self.controller.on_button_click('C')
        self.mock_view.value_var.get().asseert_called_once(textwrap='')

    def test_add(self):
        self.controller.on_button_click('+')
        self.mock_view.value_var.get().asseert_called_once(textwrap='+')

    def test_subs(self):
        self.controller.on_button_click('-')
        self.mock_view.value_var.get().asseert_called_once(textwrap='-')

    def test_multiply(self):
        self.controller.on_button_click('*')
        self.mock_view.value_var.get().asseert_called_once(textwrap='*')

    def test_divide(self):
        self.controller.on_button_click('/')
        self.mock_view.value_var.get().asseert_called_once(textwrap='/')

    def test_add_arg(self):
        params = '0123456789'
        for i in params:
            self.controller.on_button_click(int(i))
            self.mock_view.value_var.get().asseert_called_once(textwrap=i)

    def test_run(self):
        self.controller.main()
        self.mock_view.main.asseert_called_once()



