import sys
import time
import numpy as np

arr1 = np.array([1,2,3,4,5,6])
arr2 = np.array([4,5,6,7,8,9])

print(arr1 - arr2)
print("<->")
print(arr1 * arr2)    # dot product
print("<->")
print(arr1 * 2)       # scalor multiplication
print("<->")
print(arr1 > 3)

arr3 = np.arange(6).reshape(2,3)
arr4 = np.arange(6,12).reshape(3,2)

print("<->")
print(arr3.dot(arr4))

print(arr4.max())
print("<->")
print(arr4.min(axis=0))       # column wise minimum 
print("<->")
print(arr4.min(axis=1))       # row wise minimum
print("<->")
print(arr4.sum())
print("<->")
print(arr4.sum(axis=0))
print("<->")
print(arr4.mean())
print("<->")
print(arr4.std())
print("<->")
print(np.sin(arr4))
print("<->")
print(np.median(arr4))
print("<->")
print(np.exp(arr4))

### OUTPUT 

"""
[-3 -3 -3 -3 -3 -3]
<->
[ 4 10 18 28 40 54]
<->
[ 2  4  6  8 10 12]
<->
[False False False  True  True  True]
<->
[[ 28  31]
 [100 112]]
11
<->
[6 7]
<->
[ 6  8 10]
<->
51
<->
[24 27]
<->
8.5
<->
1.707825127659933
<->
[[-0.2794155   0.6569866 ]
 [ 0.98935825  0.41211849]
 [-0.54402111 -0.99999021]]
<->
8.5
<->
[[  403.42879349  1096.63315843]
 [ 2980.95798704  8103.08392758]
 [22026.46579481 59874.1417152 ]]
"""
