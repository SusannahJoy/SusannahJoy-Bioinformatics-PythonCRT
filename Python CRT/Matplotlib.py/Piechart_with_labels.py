import numpy as np
import matplotlib.pyplot as plt
y=np.array([35,25,25,15])
mylabels=["Apples","Bananas","Cherries","Dates"]
myexplode=[0,0,0.1,0]
plt.pie(y,labels=mylabels,startangle=360,explode=myexplode)
plt.legend(title="Four Fruits:")
plt.show()