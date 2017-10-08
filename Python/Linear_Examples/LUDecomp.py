import scipy.linalg as sciLA
import numpy as np

A = np.array([[2,4,-1,5,-2],[-4,-5,3,-8,1],[2,-5,-4,1,8],[-6,0,7,-3,1]])
A
P, L, U = sciLA.lu(A)

print(P)
print(L)
print(U)
