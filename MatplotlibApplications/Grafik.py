import matplotlib.pyplot as plt
import numpy as np

ort1= int(input("1. Ortalama="))
ort2= int(input("2. Ortalama="))
ort3= int(input("3. Ortalama="))
ort4= int(input("4. Ortalama="))

x=np.array(["1.Ortalama", "2. Ortalama","3. Ortalama","4. Ortalama"])
y=np.array([ort1,ort2,ort3,ort4])

plt.bar(x,y)
plt.show()