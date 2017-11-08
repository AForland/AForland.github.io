import numpy as np
from sympy import Matrix as M

A = np.array(input('What is the Matrix?:' ))
A = np.array(A)
print(A)



np.linalg.det(A)

for M in A:
    if M.det() == 0:
        print("not invertible")
    else:
        z = M.inv()
        print(z)
