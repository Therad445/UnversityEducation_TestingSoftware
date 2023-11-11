import tkinter as tk


class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero!")
        return x / y

    def exponent(self, x, y):
        return x ** y

    def square_root(self, x):
        if x < 0:
            raise ValueError("Cannot take square root of negative number!")
        return x ** 0.5


class Model:
    def __init__(self):
        self.calculator = Calculator()
        self.current_value = 0
        self.operation = None

    def set_operation(self, operation):
        self.operation = operation

    def clear(self):
        self.current_value = 0
        self.operation = None

    def calculate(self, value):
        if self.operation == 'add':
            self.current_value = self.calculator.add(self.current_value, value)
        elif self.operation == 'subtract':
            self.current_value = self.calculator.subtract(self.current_value, value)
        elif self.operation == 'multiply':
            self.current_value = self.calculator.multiply(self.current_value, value)
        elif self.operation == 'divide':
            self.current_value = self.calculator.divide(self.current_value, value)
        elif self.operation == 'exponent':
            self.current_value = self.calculator.exponent(self.current_value, value)
        elif self.operation == 'square_root':
            self.current_value = self.calculator.square_root(self.current_value)
        self.operation = None


class View:
    def __init__(self, controller):
        self.controller = controller
        self.root = tk.Tk()
        self.root.title("Calculator")
        self.result = tk.Label(self.root, text="0", width=20, height=2, font=("Arial", 20))
        self.result.grid(row=0, column=0, columnspan=4)
        self.create_button("C", self.controller.clear, 1, 0)
        self.create_button("±", None, 1, 1)
        # self.create_button("√", self.controller.square_root, 1, 2)
        self.create_button("/", lambda: self.controller.set_operation('divide'), 1, 3)
        self.create_button("7", lambda: self.controller.calculate(7), 2, 0)
        self.create_button("8", lambda: self.controller.calculate(8), 2, 1)
        self.create_button("9", lambda: self.controller.calculate(9), 2, 2)
        self.create_button("*", lambda: self.controller.set_operation('multiply'), 2, 3)
        self.create_button("4", lambda: self.controller.calculate(4), 3, 0)
        self.create_button("5", lambda: self.controller.calculate(5), 3, 1)
        self.create_button("6", lambda: self.controller.calculate(6), 3, 2)
        self.create_button("-", lambda: self.controller.set_operation('subtract'), 3, 3)
        self.create_button("1", lambda: self.controller.on_number_clicked(1), 4, 0)
        self.create_button("2", lambda: self.controller.on_number_clicked(2), 4, 1)
        self.create_button("3", lambda: self.controller.calculate(3), 4, 2)
        self.create_button("+", lambda: self.controller.set_operation('add'), 4, 3)
        self.create_button("0", lambda: self.controller.calculate(0), 5, 0, columnspan=2)
        self.create_button(".", None, 5, 2)
        self.create_button("=", self.controller.calculate, 5, 3)

    def create_button(self, text, command, row, column, columnspan=1):
        button = tk.Button(self.root, text=text, width=5, height=2, font=("Arial", 20), command=command)
        button.grid(row=row, column=column, columnspan=columnspan)

    def update_result(self, value):
        self.result.config(text=str(value))

    def run(self):
        self.root.mainloop()


class Controller:
    def __init__(self, model):
        self.model = model

    def set_operation(self, operation):
        self.model.set_operation(operation)

    def clear(self):
        self.model.clear()
        self.view.update_result(0)

    def calculate(self, value):
        self.model.calculate(value)
        self.view.update_result(self.model.current_value)

    def square_root(self):
        self.model.set_operation('square_root')
        self.view.update_result(self.model.current_value)


if __name__ == '__main__':
    model = Model()
    controller = Controller(model)
    view = View(controller)
    view.run()
