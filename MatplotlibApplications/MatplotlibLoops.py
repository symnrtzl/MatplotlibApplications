import matplotlib.pyplot as plt
import numpy as np
from numpy import random

x=[]
y=[]

for a in range(20):
    y.append(random.randint(50))
    x.append(a)

x1=np.array(x)
y1=np.array(y)

plt.plot(x1,y1, marker='o')
plt.show()
