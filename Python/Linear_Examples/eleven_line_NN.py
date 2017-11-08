import numpy as np
import matplotlib as plt

X = np.array([ [0,0,1],
               [0,1,1],
               [1,0,1],
               [1,1,1] ])

y = np.array([[0,1,1,0]]).T

syn0 = 2*np.random.random((3,4)) - 1
syn1 = 2*np.random.random((4,1)) - 1

def sigmoid(vector):
    return 1/(1+np.exp(-(vector)))


for j in range(60000):
    h1 = np.dot(X,syn0)

    l1 = sigmoid(h1)

    h2 = np.dot(l1,syn1)


    l2 = sigmoid(h2)
    l2_delta = (y - l2) #*(l2*(1-l2))
    l1_delta = l2_delta.dot(syn1.T)  * (l1 * (1-l1))

    syn1 += l1.T.dot(l2_delta)
    syn0 += X.T.dot(l1_delta)

print(l2_delta.dot(syn1.T) )
print(l1  * (1 - l1))


print(l2)
