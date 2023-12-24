"""
Crated on Oct 30 2023

@author: Islamov Radmir therad445
"""
from model import Model
from view import View


class Controller:

    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def main(self):
        self.view.main()

    def on_button_click(self, caption):
        self.result = self.model.calculate(caption)
        self.view.value_var.set(self.result)


if __name__ == "__main__":
    calculator = Controller()
    calculator.main()
