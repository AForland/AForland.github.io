import numpy as np

L = np.array([[1,0,0],[-3,1,0],[2,3,1]])
U = np.array([[2,0,5,2],[0,3,2,3],[0,0,0,4]])

#Two ways to apply this product
np.dot(L,U)
A.dot(B)

# Note not the same as above
np.dot(B,A)

# Not compatable
np.dot(A,C)
np.dot(C,A)
