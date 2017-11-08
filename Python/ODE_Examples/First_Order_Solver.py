from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
import math

# Define a function which calculates the derivative
def dy_dx(y, x):
    return np.log(1+ x^2 + y^2)

i = 0
while(i < 10):
    xs = np.linspace(0,50,100)
    y0 = i
    ys = odeint(dy_dx, y0, xs)
    ys = np.array(ys).flatten()
    plt.plot(xs, ys)
    i = i +1

plt.xlabel("x")
plt.ylabel("y");

plt.show()
