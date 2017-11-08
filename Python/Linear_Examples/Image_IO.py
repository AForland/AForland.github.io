import numpy as np
from PIL import Image

Edg = 200 # Length of the side of the image
SIZE = Edg**2
A = np.empty(shape = (SIZE,0))

np.size(Image.open('/home/wildpanic/GitProjects/Breast-Cancer-Machine-Learning/Images/Test_Data/Paint1.png'))

for i in range(1,5):
    im = Image.open('/home/wildpanic/GitProjects/Breast-Cancer-Machine-Learning/Images/Test_Data/Paint'+str(i)+'.png') # + str(x) +".png"') # open the image for the character to test
  # im = Image.open("/Letters\\"+str(i)+".png") # open the image each loop
    F = list(im.getdata()) # make the image into a list of (x,x,x) of grey scale values for x
    L1  = [x[0] for x in F] # takes the first entry of each QUAD
    L2 = [abs(x - 255.0) for x in L1] # flips the white and black pixels
    L3 = np.array(L2).T
    A = np.c_[A,L3]
    # print(A.T)

#save to a csv. 
np.savetxt("/home/wildpanic/GitProjects/Breast-Cancer-Machine-Learning/Test.csv", A , delimiter = ',')
