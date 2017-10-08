import numpy as np

L = np.array([[6,15],[0,23]])
U = np.array([[1,0],[-3/2,1]])
C = np.array([[1,2],[2,-2], [3,4]])

#Two ways to apply this product
np.dot(L,U)
A.dot(B)

# Note not the same as above
np.dot(B,A)

# Not compatable
np.dot(A,C)
np.dot(C,A)
