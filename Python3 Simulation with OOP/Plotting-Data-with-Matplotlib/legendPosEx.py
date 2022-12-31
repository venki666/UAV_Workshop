#legendPosEx.py
import matplotlib.pyplot as plt
import numpy as np

# close all the figures, if open from previous commands
plt.close('all') 

ur = np.random.rand(100)
nr = np.random.randn(100)
x=np.linspace(0,3, 100)

ax = plt.subplot(1,1,1)

ax.plot(x, label="Line")
ax.plot(ur, label="Uniform random number")
ax.plot(nr, label="Normal random number")
ax.set_title("Legend outside the plot")

# Plot position and shriking to create space for legends
box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.2,
                 box.width, box.height * 0.8])

# Add legend below the axis
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
          fancybox=True, shadow=True, ncol=2)

plt.show()