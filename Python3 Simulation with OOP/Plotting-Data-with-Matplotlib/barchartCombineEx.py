#barchartCombineEx.py
import numpy as np
import matplotlib.pyplot as plt

plt.close("all")

#### subplot 1
A = [2, 4, 8, 6]
increment = [5, 6, 4, 1]
years = [2005, 2010, 2015, 2020]

plt.subplot(2,1,1)
plt.bar(years, A, color = 'b', label='A')
plt.bar(years, increment, color = 'r', bottom = A, label='increment')
plt.legend()

plt.show()

##### subplot 2
x = [1, 2, 4]
y = [3.5, 3, 2]
z = [2, 3, 1.5]

width = 0.2
locs = np.arange(1, len(x)+1)
plt.subplot(2,1,2)
plt.bar(locs, x, width=width, label='x')
plt.bar(locs+width, y, width=width, color="red", label='y')
plt.bar(locs+2*width, z, width=width, color="black", label='z')
plt.legend()

plt.xticks([1.25, 2.25, 3.25],
          [r'$2000$', r'$2005$', r'$2010$'])

plt.show()