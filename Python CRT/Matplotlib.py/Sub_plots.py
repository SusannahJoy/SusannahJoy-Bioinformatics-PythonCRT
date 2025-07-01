import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt
#plot 1:
x=np.array([0,1,2,3])
y=np.array([3,8,1,10])
plt.subplot(2,3,1)
plt.title("Plot-1")
plt.plot(x,y)
#plot 2
x=np.array([0,1,2,3])
y=np.array([10,20,30,40])
plt.subplot(2,3,2)
plt.title("Plot-2")
plt.plot(x,y)
#plot 3
x=np.array([0,1,2,3])
y=np.array([3,8,1,10])
plt.subplot(2,3,3)
plt.title("Plot-3")
plt.plot(x,y)
#plot 4
x=np.array([0,1,2,3])
y=np.array([10,20,30,40])
plt.subplot(2,3,4)
plt.title("Plot-4")
plt.plot(x,y)
#plot 5
x=np.array([0,1,2,3])
y=np.array([3,8,1,10])
plt.subplot(2,3,5)
plt.title("Plot-5")
plt.plot(x,y)
#plot 6
x=np.array([0,1,2,3])
y=np.array([10,20,30,40])
plt.subplot(2,3,6)
plt.title("Plot-6")
plt.plot(x,y)
plt.suptitle("My Shop")
plt.show()