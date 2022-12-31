#arangeEx.py
import numpy as np
a=np.arange(1,10) # last element i.e. 10 is not included in result
print(a) # [1 2 3 4 5 6 7 8 9]
print(a.shape) # (9,) i.e. total 9 entries

b=np.arange(1,10,2) # print 1 to 10 with the spacing of 2
print(b) # [1 3 5 7 9]
print(b.shape) # (5,) i.e. total 9 entries

c=np.arange(10, 2, -2) # last element 2 is not included in result self
print(c) # [10  8  6  4]