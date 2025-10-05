import sys            # importing system 
import time           # to measure speed 
import numpy as np

lista = range(100)
arr1 = np.arange(100)

print(sys.getsizeof(87)*len(lista))
print(arr1.itemsize*arr1.size)

x = range(10000000)
y = range(10000000, 20000000)

start_time = time.time()

# Adding both and creating a new list 
c = [x+y for x,y in zip(x,y)]       # Adding both the arrays index-wise 

print(time.time() - start_time)     # duration for which the code ran 

a = np.arange(10000000)
b = np.arange(10000000, 20000000)

start_time = time.time()
c = a + b       # c itself will be NumPy Array 

print(time.time() - start_time)

"""
  -> Lists occupy more memory 
  -> Lists take more time for execution
"""
