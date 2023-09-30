import matplotlib.pyplot as plt
import numpy as np

x=np.array([0,1,2,3,4,5])
y=np.array([5,15,1,20,8,10])
x2=np.array([0,1,2,3,4,5])
y2=np.array([1,4,8,2,10,3])

plt.plot(x,y,x2,y2,marker='o')

plt.show()