import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,7,5,3,2])
y=np.array([50,120,10,20,80])
#boyut=np.array([150,10,100,80,5])
boyut=np.array([y[0],y[1],y[2],y[3],y[4]])

plt.scatter(x,y, s=boyut) #s=size
plt.show()