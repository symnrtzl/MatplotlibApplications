import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

figure, grafik1=plt.subplots()
grafik1.set_xlim([0,10])

scat= grafik1.scatter(0,0)
scat2= grafik1.scatter(0,1)
scat3=grafik1.scatter(0,0.5)
grafik1=np.linspace(0,10,200)

def animate(i):
    scat.set_offsets((grafik1[i],0))
    scat2.set_offsets((grafik1[i],1))
    scat3.set_offsets((grafik1[i+20],0.5))
    print(i)
    return scat,

animation=animation.FuncAnimation(figure, animate, repeat=True, frames=len(grafik1)-1,interval=10)
plt.show()