import unittest
from view import View
from presenter import Controller


class TestView(unittest.TestCase):
    def setUp(self):
        self.controller = Controller()
        self.view = View(self.controller)
    
    def test_window_title(self):
        self.assertEqual(self.view.title(), 'PyTkCalc')

    def test_button_captions(self):
        expected_captions = [
            'C', '+/-', '%', '/',
            7, 8, 9, '*',
            4, 5, 6, '-',
            1, 2, 3, '+',
            0, '.', '='
        ]
        actual_captions = [btn['text'] for btn in self.view.winfo_children() if btn.winfo_class() == 'TButton']
        self.assertEqual(expected_captions, actual_captions)
    
    def test_entry_field(self):
        entry = self.view.winfo_children()[0]
        self.assertEqual(entry.winfo_class(), 'TFrame')
        self.assertEqual(entry['state'], 'disabled')
    
    def test_value_var(self):
        self.view.controller.on_button_click(1)
        self.assertEqual(self.view.value_var.get(), '1')
        self.view.controller.on_button_click('+')
        self.assertEqual(self.view.value_var.get(), '')
        self.view.controller.on_button_click(2)
        self.assertEqual(self.view.value_var.get(), '2')
        self.view.controller.on_button_click('=')
        self.assertEqual(self.view.value_var.get(), '3')