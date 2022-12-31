#subplotEx2.py
import numpy as np
import matplotlib.pyplot as plt

N=100
x=np.arange(N)
rn = np.random.randn(N)
r = np.random.rand(N)

# create an object 'fig1'  of figure() 
fig1 = plt.figure()

# create two instances of fig1
subfig1 = fig1.add_subplot(2,1,1)
subfig2 = fig1.add_subplot(2,1,2, sharey = subfig1) #share y axis

# plot figures
subfig1.plot(x, rn)
subfig2.plot(x, r)
plt.show()