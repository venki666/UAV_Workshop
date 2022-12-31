#numpyDataEx.py
# import numpy library with short name `np'
# outputs are shown as comments
import numpy as np

# 1. linspace(a, b, total_points)
x = np.linspace(2, 8, 4) 
print(x) # [ 2.  4.  6.  8.]

# 2. sin(x)
sinx = np.sin(x) # x is consider as radian
print(sinx) # [ 0.90929743 -0.7568025  -0.2794155   0.98935825]

# 3. cos(x)
cosx = np.cos(x)
print(cosx) #[-0.41614684 -0.65364362  0.96017029 -0.14550003]

# 4. rand: uniform random variables
ur = np.random.rand(4) # result below will be different as it is random
print(ur) # [ 0.99791448  0.95621806  0.48124676  0.20909043]

# 5. randn: normal random variables
nr = np.random.randn(4) # result below will be different as it is random
print(nr) # [-0.37188868 -0.5680135  -0.21731407 -0.69523557]
