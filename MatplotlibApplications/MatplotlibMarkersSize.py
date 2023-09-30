import matplotlib.pyplot as plt
import numpy as np

y=np.array([5,15,1,20,8,10,4])

#plt.plot(y, marker='o')
#plt.plot(y, '*--',ms=2)
#plt.plot(y, '1--r',ms=10)
#plt.plot(y, '*--',ms=5)
#plt.plot(y, 'o:g',ms=2) # şekil,çizgi,renk
plt.plot(y, 'o-.g', ms=5) # --*--*--*--*
plt.show()