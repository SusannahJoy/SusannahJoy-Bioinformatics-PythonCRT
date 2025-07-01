'''
Write a python program to create a 1D array with 15 elements and 
a) reshape it into 2D array with 3 rows and 5 coloumns
b) 5 rows and 3 coloumns and print dimension of it
c) reshape the same array into a 3D array with 5 rows and 3 coloumns with 1 element in each coloumn
'''
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
#3 rows and 5 coloumns
newarr=arr.reshape(3,5)
print(newarr)
#5 rows and 3 coloumns
newarr1=arr.reshape(5,3)
print(newarr1)
#3D with 5 rows and 3 coloumns
newarr2=arr.reshape(5,3,1)
print(newarr2)