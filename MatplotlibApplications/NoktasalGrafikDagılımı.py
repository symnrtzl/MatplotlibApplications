import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,27,18])
y=np.array([50,20,60,50,80,40,70,100,30,25,68,98,90,12,14,60,100,60])

plt.scatter(x,y) # noktasal olarak bir grafiğin dağılımı yapılırken scatter kullanılır
#x=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,27,18])
#y=np.array([60,10,40,90,30,80,50,80,20,60,80,90,90,20,40,70,90,40])

plt.scatter(x,y)
plt.show()