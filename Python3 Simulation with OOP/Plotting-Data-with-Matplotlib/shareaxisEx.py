#shareaxisEx.py
import numpy as np
import matplotlib.pyplot as plt

N=100
x=np.linspace(0.1,4, N)
e1 = np.exp(x)
e2 = np.exp(-x)

# create an object 'fig1'  of figure() 
fig1 = plt.figure()

# create two instances of fig1 at location 1,1,1
subfig1 = fig1.add_subplot(1,1,1)
subfig2 = fig1.add_subplot(1,1,1)

# share the x-axis for both plot
subfig2 = subfig1.twinx()

# plot subfig1
# semilogy for log 'y' axis, for log x use semilogx
subfig1.semilogy(x, e1) 
subfig1.set_ylabel("log scale: exp(x)")
subfig1.set_xlabel("x-->")

# plot subfig2
subfig2.plot(x, e2, 'r')
subfig2.set_ylabel("simple scale: exp(-x)")

plt.show()