import sys 
import time
import numpy as np

arr1 = np.arange(24).reshape(6,4)
print(arr1)
print("<->")
print(arr1[[0,2,4]])        # extracting particular rows with index 0,2,4
print("<->")
arr = np.random.randint(low=1, high=100, size=20).reshape(4,5)    # reshaped in 4 X 5 2D Array <-
print(arr)
print("<->")
print(arr[0])
print("<->")
print(arr > 50)     # individual checking and it will return true or false <-
print("<->")
print(arr[arr > 50])  # filtering elements from the array <- 
print("<->")
print(arr[(arr > 50) & (arr%2 != 0)])     # we can manipulate the array in n number of ways <-
print("<->")
arr[(arr > 50) & (arr%2 != 0)] = 0        # replace those elements by 'zero' <-
print(arr)

# OUTPUT <- 
"""
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]
 [16 17 18 19]
 [20 21 22 23]]
<->
[[ 0  1  2  3]
 [ 8  9 10 11]
 [16 17 18 19]]
<->
[[36  6  9 94 50]
 [94 22 55 46 41]
 [47 56 77 43  7]
 [56 76 92 43 21]]
<->
[36  6  9 94 50]
<->
[[False False False  True False]
 [ True False  True False False]
 [False  True  True False False]
 [ True  True  True False False]]
<->
[94 94 55 56 77 56 76 92]
<->
[55 77]
<->
[[36  6  9 94 50]
 [94 22  0 46 41]
 [47 56  0 43  7]
 [56 76 92 43 21]]
"""
