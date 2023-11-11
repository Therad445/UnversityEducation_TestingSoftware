class Model:

    def __init__(self):
        self.previous_value = ''
        self.value = ''
        self.operator = ''

    def calculate(self, caption):
        if caption == 'C':
            self._clear()

        elif caption == '+/-':
            self._change_type()

        elif caption == "%":
            value = float(self.value) if '.' in self.value else int(self.value)
            self.value = str(value / 100)

        elif caption == "=":
            value = self._evaluate()
            if '.0' in str(value):
                value = int(value)
            self.value = str(value)

        elif caption == ".":
            self._decimal(caption)

        elif isinstance(caption, int):
            self.value += str(caption)

        else:
            if self.value:
                self.operator = caption
                self.previous_value = self.value
                self.value = ''

        return self.value

    def _evaluate(self):
        if self.operator == '+':
            return self._sum()
        elif self.operator == '-':
            return self._subtract()
        elif self.operator == '*':
            return self._multiply()
        elif self.operator == '/':
            return self._div()

    def _sum(self):
        return float(self.previous_value) + float(self.value)

    def _subtract(self):
        return float(self.previous_value) - float(self.value)

    def _multiply(self):
        return float(self.previous_value) * float(self.value)

    def _div(self):
        return float(self.previous_value) / float(self.value)

    def _change_type(self):
        self.value = self.value[1:] if self.value[0] == '-' else '-' + self.value

    def _clear(self):
        self.previous_value = ''
        self.value = ''
        self.operator = ''

    def _decimal(self, caption):
        if caption not in self.value:
            self.value += caption
