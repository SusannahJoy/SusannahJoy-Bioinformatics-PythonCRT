import numpy as np
arr=np.array([1,2,3,4,5,6])
newarr=np.array_split(arr,3)
print("Original Array :",arr)
print("Splitted Array :",newarr)
print("----------------------------")
#splitting array into 4 parts
import numpy as np
arr=np.array([1,2,3,4,5,6])
newarr1=np.array_split(arr,4)
print("Original Array :",arr)
print("Splitted Array :",newarr1)
print("----------------------------")
#splitting 2D arrays:
import numpy as np
arr=np.array([[1,2],[3,4],[5,6],[7,8],[9,10]])
newarr=np.array_split(arr,3)
print("Original Array :",arr)
print("Splitted Array :",newarr)