import numpy as np
import matplotlib.pyplot as plt
import scipy.special
from PIL import Image
import pandas as pd

def character_check(im):

    activation_function = lambda x: scipy.special.expit(x)

    F = list(im.getdata()) # make the image into a list of (x,x,x) of grey scale values for x
    L1  = [x[0] for x in F] # takes the first entry of each triple
    L2 = [abs(x - 255.0) for x in L1]

    np.shape(L2)

    who = np.loadtxt('/home/adam/Documents/Python/who.csv')
    wih = np.loadtxt('/home/adam/Documents/Python/wih.csv')

    np.shape(who)
    np.shape(wih)

    E = np.dot(wih,L2)
    E = activation_function(E)
    Out = np.dot(who,E)
    Out = activation_function(Out)

    return Out

def sigmoid(x):
    return scipy.special.expit(x)
t1 = np.arange(-5.0, 5.0, 0.1)

plt.plot(t1, sigmoid(t1), 'k')
plt.show()

img = Image.open("/home/adam/Documents/Python/letters/two.bmp")
img

display = pd.DataFrame({'Prob': character_check(img)})
display
