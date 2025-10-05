# To understand how to use NumPy Functions
# Creating numpy/n-d arrays 
import numpy as np

arr1 = np.array([1,2,3,4,5])
arr1
type(arr1)

arr2 = np.array([[1,2,3],[4,5,6]])
arr2

arr3 = np.zeros((2,3))
arr3

arr4 = np.ones((3,3))
arr4
# By Default 

arr5 = np.identity(5)
arr5

arr6 = np.arange(10)
arr6

arr7 = np.arange(5,16,2)
arr7

arr8 = np.linspace(10,20,10)    # equispaced points between given two numbers (a,b,d) => d is the difference
arr8

arr9 = arr8.copy()
arr9

# -> Shape of Array <- 
# Shapes
arr1.shape

arr2.shape

arr10 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
arr10

arr10.shape   # 3 dimension 

arr10.ndim

arr9.size 

arr8.itemsize       # size of items 

arr8.dtype

arr9.astype('float')      # when to use it? It can be used to clean data => Example Age is stored in float can be reduced to "INT"
