#arrayEx.py
import numpy as np

a= np.array([1, 8, 2])
print(a) # [1 8 2]
print(np.shape(a)) # (3,)
b=np.array([
  [1, 2],
  [4, 3],
  [6, 2]
])
#b can be written as follow as well, but above is more readable
# b=np.array([[1, 2],[4, 3]])
print(np.shape(b)) #(3, 2) i.e. 3 row and 2 column