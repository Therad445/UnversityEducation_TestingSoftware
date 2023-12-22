import numpy as np
import matplotlib.pyplot as plt

# Определение функции
def f(x):
    return 5 * x**4 + x**3 + x**2 + 2*x - 2

# Создание массива значений x
x = np.linspace(-2, 2, 1000)

# Построение графика функции
plt.plot(x, f(x))
plt.axhline(0, color='black', lw=0.5, linestyle='--')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('График уравнения 5x^4 + x^3 + x^2 + 2x - 2')
plt.grid(True)
plt.show()