#firstPlotGL.py
import numpy as np
import matplotlib.pyplot as plt

# close all the figures, if open from previous commands
plt.close('all') 

############ Sin(x) ####################
x=np.linspace(-2*np.pi, 2*np.pi, 100) 
sinx=np.sin(x) # calculate sin(x)
plt.plot(x,sinx, label='sin')

############ Legend ####################
# label in plt.plot are displayed by legend command 
plt.legend(loc="best") #show legend

#### Lable and Grid ####################
plt.xlabel("Radian") # x label 
plt.ylabel("Amplitude") # y label

plt.grid() # show grid

plt.show() #display the plot