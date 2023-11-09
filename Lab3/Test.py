import unittest
from unittest.mock import patch
from controller import Controller

class TestController(unittest.TestCase):
    def setUp(self):
        self.controller = Controller()
    
    @patch('view.View.display_error')
    def test_on_button_click_display_error(self, mock_display_error):
        self.controller.on_button_click('/')
        mock_display_error.assert_called_once()
    
    @patch('view.View.display_result')
    def test_on_button_click_display_result(self, mock_display_result):
        self.controller.on_button_click('=')
        mock_display_result.assert_called_once()
    
    @patch('view.View.display_error')
    def test_on_button_click_division_by_zero(self, mock_display_error):
        self.controller.on_button_click('7')
        self.controller.on_button_click('/')
        self.controller.on_button_click('0')
        self.controller.on_button_click('=')
        mock_display_error.assert_called_once()