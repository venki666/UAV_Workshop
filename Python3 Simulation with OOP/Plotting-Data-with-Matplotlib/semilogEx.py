#semilogEx.py
import numpy as np
import matplotlib.pyplot as plt

# close all the figures, if open from previous commands
plt.close('all') 

x=np.linspace(0.01, 5, 100)
e=np.exp(x)

#linear plot
plt.plot(x,e)
plt.xlabel("x")
plt.ylabel("y=exp(x)")
plt.title("Linear Y axis")

#semilog plot
#log(exp(x))=x therefore straight line will be displayed
plt.figure()
plt.semilogy(x,e) #semilogy: semilog y-axis
plt.xlabel("x")
plt.ylabel("y=exp(x)") 
plt.title("Log Y axis")
             
plt.show() #display the plot
