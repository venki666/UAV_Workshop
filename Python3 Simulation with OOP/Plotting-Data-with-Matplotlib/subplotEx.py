#subplotEx.py
import numpy as np
import matplotlib.pyplot as plt

# close all the figures, if open from previous commands
plt.close('all') 

############ Sin(x) ####################
x=np.linspace(-2*np.pi, 2*np.pi, 100) 
sinx=np.sin(x) # calculate sin(x)
cosx=np.cos(x) # calculate cos(x)

########### Subplot ###################
plt.subplot(2,1,1)
plt.plot(x,sinx, '*--r', label='sin')
plt.grid() # show grid
plt.legend() #show legend
plt.xlabel(r'$Radian$')# x label 
plt.ylabel(r'$Amplitude$') # y label

plt.subplot(2,1,2)
plt.plot(x,cosx, 'o-g', label='cos') 
plt.grid() # show grid
plt.legend() #show legend
plt.xlabel(r'$Radian$') # x label 
plt.ylabel(r'$Amplitude$') # y label
############ Legend ####################

#### Lable and Grid ####################
plt.xlabel(r'$Radian$') # x label 
plt.ylabel(r'$Amplitude$') # y label


plt.show()