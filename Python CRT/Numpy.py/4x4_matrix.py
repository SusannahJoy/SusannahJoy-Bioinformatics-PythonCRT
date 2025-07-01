'''
Write a Python program to create a matrix with 4 rows and 4 coloumns using numpy library 
and give multiples of 5
'''
import numpy as np
arr=np.array([5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80])
newarr=arr.reshape(4,4)
print(newarr)