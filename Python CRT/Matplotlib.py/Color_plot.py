import numpy as np
import matplotlib.pyplot as plt
x=np.array([5,7,4,2,17,2,9,4,11,12])
y=np.array([99,86,87,88,111,86,103,87,94,78])
colors=np.array([10,20,30,40,50,60,70,80,90,100])
plt.scatter(x,y,c=colors,cmap='viridis')
plt.show()