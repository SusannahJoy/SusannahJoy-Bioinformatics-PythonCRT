#Array[start:end]
#Array[start:end:stepsize]
#Array[:end]
import numpy as np
arr=np.array([1,2,3,4,5,6,7])
print(arr[1:5])
print(arr[2:4])
#Negative slicing
import numpy as np
arr=np.array([1,2,3,4,5,6,7])
print(arr[-3:-1])
#2D slicing
import numpy as np
arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[1,1:4])