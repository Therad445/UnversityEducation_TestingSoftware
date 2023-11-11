"""
Crated on Oct 30 2023

@author: Islamov Radmir therad445
"""
from model import Model
from view import View


class Controller:

    def __init__(self, model, view):
        super().__init__()
        self.model = model()
        self.view = view(self)

    def main(self):
        self.view.main()

    def on_button_click(self, caption):
        result = self.model.calculate(caption)
        self.view.value_var.set(result)


if __name__ == "__main__":
    calculator = Controller(Model, View)
    calculator.main()
