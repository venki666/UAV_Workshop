#reduceEx.py
from functools import reduce
num = [1, 2, 3, 4, 5]
sumNum = reduce((lambda x, y: x + y), num)
print(sumNum) #15