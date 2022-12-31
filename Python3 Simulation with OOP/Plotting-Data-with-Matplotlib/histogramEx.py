#histogramEx.py
import numpy as np
import matplotlib.pyplot as plt

plt.close("all")

ur = np.random.rand(10000)
nr = np.random.randn(10000)

plt.subplot(2,2,1)
plt.hist(ur)
plt.xlabel("Uniform Random Number, Default 10 Bin")

plt.subplot(2,2,2)
plt.hist(ur, 20) # display 20 bins
plt.xlabel("Uniform Random Number, 20 Bin")

plt.subplot(2,2,3)
plt.hist(nr)
plt.xlabel("Normal Random Number, Default 10 Bin")

plt.subplot(2,2,4)
plt.hist(nr, 20) # display 20 bins
plt.xlabel("Normal Random Number, 20 Bin")

plt.show()