from sympy import symbols
from sympy import *
from numpy import linspace
from sympy import lambdify
import matplotlib.pyplot as mpl

t = symbols('t')
x = 1/sqrt(3.14) * exp(-1/2 * t**2)
lam_x = lambdify(t, x, modules=['numpy'])

x_vals = linspace(-3, 3, 100)
y_vals = lam_x(x_vals)

mpl.plot(x_vals, y_vals)
mpl.ylabel("Speed")
mpl.show()
