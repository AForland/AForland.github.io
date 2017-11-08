import numpy as np
import matplotlib.pyplot as plt

h = 0.001 # Change in x
i = 2000 # Number of approximations to find
x = 0 # Start x_0
y = 2 # Start y_0

# The differntial RHS
def The_Derivative(x,y):
    return 7*np.e**(4*x) - 3*y

# Eulers Methiod encoded
def Eulers_Approx_Value(x,y):
        Ye = y + h * (The_Derivative(x,y))
        return Ye

# This should be the computed soultion if you have it. If not, comment this out.
def The_Answer(t):
    return np.e**(4*t) + np.e**(-3*t)

# Set Counter
j = 0

# Start and array for the x and y values
P = np.array([[x,y]])

# Loop and compute the approximations
while(j < i):
    y = Eulers_Approx_Value(x,y)
    x = x + h
    P = np.append(P , np.array([x,y]))
    j = j + 1

# reset the counter
j = 0

# Print the last value
print(y)

X = P[::2] # X values for the array
Y = P[1::2] # Y values for the array

print(Y)

# Plot the solution. If you don't have this, comment it out.
t1 = np.arange(0.0, 2.01, 0.00001)
print(t1[33])
plt.plot(t1, The_Answer(t1))

#Plot the approximations
plt.plot(X ,Y , 'r+')
plt.show()
