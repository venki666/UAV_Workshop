#completeBasicEx.py
import numpy as np
import matplotlib.pyplot as plt

# close all the figures, if open from previous commands
plt.close('all') 

############ Sin(x) ####################
x=np.linspace(-2*np.pi, 2*np.pi, 100) 
sinx=np.sin(x) # calculate sin(x)

########### Line style and Marker ###################
plt.plot(x,sinx, '*--r', markersize=10, label='sin')  

############ Legend ####################
plt.legend(loc="best") #show legend

#### Lable and Grid ####################
plt.xlabel("Radian") # x label 
plt.ylabel("Amplitude") # y label
plt.grid() # show grid

############ Axis Limit and Marker ##################
# x-axis and y-axis limits
plt.xlim([-2*np.pi, 2*np.pi]) # x-axis display range
plt.ylim([-1.5, 1.5]) # y-axis display range

# ticks on the axis
# display ticks in pi format rather than 3.14 format
plt.xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi],
          [r'$-2\pi$', r'$-\pi$', r'$0$', r'$+\pi$', r'2$\pi$'])
plt.yticks([-1, 0, +1])

################## Title #########################
plt.title("Plot $Sin(x)$")

plt.show()