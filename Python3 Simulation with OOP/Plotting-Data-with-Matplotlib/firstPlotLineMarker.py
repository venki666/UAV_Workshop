#firstPlotLineMarker.py
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

plt.show() #display the plot
