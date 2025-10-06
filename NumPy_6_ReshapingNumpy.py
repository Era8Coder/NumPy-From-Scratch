import sys 
import time
import numpy as np

arr3 = np.arange(6).reshape(2,3)
arr4 = np.arange(6,12).reshape(3,2)
print(arr4)
print("<->")
print(arr4.ndim)
print("<->")
print(arr4.ravel())         # changing the shape to 1D of any dimensional array
print("<->")
print(arr4.transpose())
print("<->")

# Stacking <-> Method to Combine Two Arrays 
arr5 = np.arange(12,18).reshape(2,3)
print("<->")
print(np.hstack((arr3,arr5)))       # stacking means combining them horizontally 
print("<->")
print(np.vstack((arr3,arr5)))
print("<->")
np.hsplit(arr3,3)           # horizontally do parts mein divide hona
print("<->")
np.vsplit(arr3,2)           # vertically do parts mein divide hona

# OUTPUT
"""
  [[ 6  7]
   [ 8  9]
   [10 11]]
  <->
  2
  <->
  [ 6  7  8  9 10 11]
  <->
  [[ 6  8 10]
   [ 7  9 11]]
  <->
  <->
  [[ 0  1  2 12 13 14]
   [ 3  4  5 15 16 17]]
  <->
  [[ 0  1  2]
   [ 3  4  5]
   [12 13 14]
   [15 16 17]]
  <->
  <->
  [array([[0, 1, 2]]), array([[3, 4, 5]])]
"""
