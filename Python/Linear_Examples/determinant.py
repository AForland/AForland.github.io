import numpy as np

A = np.array([[1,5,-3],[3,-3,3],[2,13,-7]])
B = np.array([[2,3,4],[0,4,2],[0,0,3]])
H = np.array([[1,1/2,1/3,1/4,1/5],[1/2,1/3,1/4,1/5,1/6],[1/3,1/4,1/5,1/6,1/7],[1/4,1/5,1/6,1/7,1/8],[1/5,1/6,1/7,1/8,1/9]])

A_I = np.linalg.inv(A)
print(A_I)
print(A)
np.dot(A_I,A)
H_I = np.linalg.inv(H)
print(H_I)


b = np.array([[0],[0],[0],[0],[1]])
np.dot(H_I, b)

print(H_I)


np.dot(A_I,A)

(np.linalg.det(A))
np.linalg.det(B)
