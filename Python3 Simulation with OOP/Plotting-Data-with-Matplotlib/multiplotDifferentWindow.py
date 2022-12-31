#multiplotDifferentWindow.py
import numpy as np
import matplotlib.pyplot as plt

# close all the figures, if open from previous commands
plt.close('all') 

############ Sin(x) ####################
x=np.linspace(-2*np.pi, 2*np.pi, 100) 
sinx=np.sin(x) # calculate sin(x)
cosx=np.cos(x) # calculate cos(x)

########### Open figure in seperate window ###################
#"Sin" is the name of figure window
# if not give i.e. plt.figure(), then 1 will be assigned to figure
# and for second plt.figure(), 2 will be assigned...
plt.figure("Sin") 
plt.plot(x,sinx, '*--r', label='sin')  
plt.figure("Cos")
plt.plot(x,cosx, 'o-g', label='cos') 
plt.figure("Sin")
plt.plot(x,cosx, 'o-g', label='cos') 

############ Legend ####################
plt.legend(loc="best") #show legend

#### Lable and Grid ####################
plt.xlabel(r'$Radian$').set_fontsize(16) # x label 
plt.ylabel(r'$Amplitude$').set_fontsize(16) # y label
plt.grid() # show grid

plt.show()