#polarplotEx.py
import numpy as np
import matplotlib.pyplot as plt

plt.close("all")

x=np.linspace(0,2*np.pi, 1000)

# polar axes is based on clipping so that r >= 0.
# therefore only 2 lobes are shown as oppose to 4 lobes. 
y = np.cos(2*x)
plt.polar(x, y)

plt.show()