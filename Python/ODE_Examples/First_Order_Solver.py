from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
import math

# Define a function which calculates the derivative
def dy_dx(y, x):
    return - y

xs = np.linspace(0,5,100)
y0 = 1.0
ys = odeint(dy_dx, y0, xs)
ys = np.array(ys).flatten()

plt.plot(xs, ys)
plt.xlabel("x")
plt.ylabel("y");

plt.show()
