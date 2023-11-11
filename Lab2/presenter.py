"""
Crated on Oct 30 2023

@author: Islamov Radmir therad445
"""
from calculator import Calculator
from view import View


class CalculatorPresenter:
    def __init__(self):
        self.model = Calculator()
        self.view = View(self)
        self.previous_value = ''
        self.value = ''
        self.operator = ''

    def set_operation(self, operator):
        self.operator = operator

    def on_clear_click(self):
        self.previous_value = ''
        self.value = ''
        self.operator = ''
        self.view.value_var.set(self.value)

    def on_plus_click(self, value):
        self.previous_value = value
        self.operator = '+'
        self.view.value_var.set(0)

    def on_minus_click(self, x, y):
        return self.model.subtract(x, y)

    def on_divide_click(self, x, y):
        return self.model.divide(x, y)

    def on_multiply_click(self, x, y):
        return self.model.multiply(x, y)

    def on_result_click(self, value):
        if self.operator == '+':
            model.add(int(self.previous_value), int(value))

    def on_number_click(self, number):
        self.value += str(number)
        self.view.value_var.set(self.value)

    def run(self):
        self.view.main()


if __name__ == "__main__":
    model = Calculator()
    presenter = CalculatorPresenter()
    presenter.run()
