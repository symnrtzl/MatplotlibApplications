import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,2,3,4,5,6])
y=np.array([5,6,12,25,1,5])

plt.title("Grafik Basligi",loc='left')  #loc:solda,sağda,ortada
plt.xlabel("x koordinati")
plt.ylabel("y koordinati")

plt.plot(x,y)
plt.show()