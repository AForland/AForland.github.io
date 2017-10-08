#Party example
import numpy as np

probability_matrix = np.array([[0,.8,.2,0,0,0],[0,.4,.1,.3,.2,0],[0,.2,.5,0,.3,0],[0,0,0,0,1,0],[0,0,0,0,0,1],[0,0,0,0,0,1]])
probability_matrix

def Run_The_Party(h):
    x = np.array([[10,0,0,0,0,0]])
    i = 0
    for i in range(1,h):
        print(np.dot(x,probability_matrix))
        x = np.dot(x,probability_matrix)

#The input for the party function is hours to run the party. [Arrive, Talk, Games, Dance, Eat, Leave]
Run_The_Party(50)
[Run_The_Party(6)
Run_The_Party(7)
Run_The_Party(8)
