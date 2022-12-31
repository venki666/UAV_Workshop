#annotateEx.py
import numpy as np
import matplotlib.pyplot as plt

# close all the figures, if open from previous commands
plt.close('all') 

############ Sin(x) ####################
x=np.linspace(0, 2*np.pi, 100) 
sinx=np.sin(x) # calculate sin(x)
plt.plot(x,sinx, label='sin') # legend 

############ Legend ####################
plt.legend(loc="best") #show legend

#### Lable and Grid ####################
plt.xlabel("Radian") # x label 
plt.ylabel("Amplitude") # y label

############# Annotate ######################
#1. 
# other arrow style 
# '-', '->', '-[', '<-', '<->', 'fancy', 'simple', 'wedge' 
#sin(pi/2)=1
plt.annotate(r'$sin(\frac{\pi}{2})=1$', 
             fontsize=16,
             xy=(1.5, 1), xytext=(1 , 0.5),
             arrowprops=dict(arrowstyle="->"),
        )

# 2. 
#=============================================================
# width: The width of the arrow in points
# frac: The fraction of the arrow length occupied by the head
# headwidth: The width of the base of the arrow head in points
# shrink: Moves the tip and the base of the arrow some percent 
# away from the annotated point and text, 
#=============================================================
#sin(3*pi/2)=-1
plt.annotate(r'$sin(\frac{3\pi}{2})=-1$', 
             fontsize=18,
             xy=(4.5, -1), xytext=(1.5 , -0.5),
             arrowprops=dict(facecolor='red', shrink = 0.04, 
                             connectionstyle="arc3,rad=.2"),
        )       
     
# 3.          
#################### Add text to plot ###########           
plt.text(5, 0.5, 'This is \nSine wave');
        
plt.show() #display the plot
