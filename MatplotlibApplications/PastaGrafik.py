import matplotlib.pyplot as plt
import numpy as np

etiket=np.array(["A","B","C","D"])
yuzdelikdeger=np.array([30,15,15,40])
enbuyuk=[0,0,0,0.1]

plt.pie(yuzdelikdeger,labels=etiket, explode=enbuyuk)
plt.show()