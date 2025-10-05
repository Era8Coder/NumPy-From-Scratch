import sys 
import time
import numpy as np

arr = np.arange(24).reshape(6,4)      # 6 X 4 OR 2 X 12 OR 3 X 8 
arr

"""
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11],
       [12, 13, 14, 15],
       [16, 17, 18, 19],
       [20, 21, 22, 23]])
"""

arr1 = np.array([1,2,3,4,5])
arr1[2]           # it will give the index

"""
np.int64(3)
"""

arr1[2:4]         # Slicing of index
"""
array([3, 4])
"""

arr1[-1]
"""
np.int64(5)
"""

arr[2]        # it gave me the row of the matrix 
"""
array([ 8,  9, 10, 11])
"""

arr[:2]         # it gave me two columns
"""
array([[0, 1, 2, 3],
       [4, 5, 6, 7]])
"""

arr[:, 2]         # first one is for extracting all the rows and second one is for extracting the second column
"""
array([ 2,  6, 10, 14, 18, 22])
"""

arr[2:4, 1:3]     # 2 -> 4 rows and 1 -> 3 cols
"""
array([[ 9, 10],
       [13, 14]])
"""

# ITERATION : 
for i in arr:
  print(i)
"""
[0 1 2 3]
[4 5 6 7]
[ 8  9 10 11]
[12 13 14 15]
[16 17 18 19]
[20 21 22 23]
"""

for i in np.nditer(arr):
  print(i)
"""
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
"""
