#numpyMatplot.py
import numpy as np
import matplotlib.pyplot as plt
# np.linspace: devide line from 0 to 4*pi into 100 equidistant points
x = np.linspace(0, 4*np.pi, 100)
sinx = np.sin(x) #find sin(x) for above 100 points
plt.plot(x,sinx) # plot (x, sin(x))
plt.xlabel("Time") # label for x axis
plt.ylabel("Amplitude") # label for y axis
plt.title('Sine wave') # title
plt.show()