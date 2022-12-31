#firstPlot.py
import numpy as np
import matplotlib.pyplot as plt

# close all the figures, if open from previous commands
plt.close('all') 

x=np.linspace(-2*np.pi, 2*np.pi, 100) 
sinx=np.sin(x) # calculate sin(x)
plt.plot(x,sinx) #plot x on x-axis and sin_x on y-axis
plt.show() #display the plot
