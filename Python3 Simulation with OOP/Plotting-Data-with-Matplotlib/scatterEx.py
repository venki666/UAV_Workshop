#scatterEx.py
import numpy as np
import matplotlib.pyplot as plt

plt.close("all")

N=100
x = np.linspace(0, 2*np.pi, N)
noise = np.random.randn(N)
signal = 2*np.sin(x)

y = signal + noise
plt.plot(x, signal) # signal + noise
plt.scatter(x, y) #scatter plot

plt.figure()
y = signal + 0.2*noise # singal + 0.2*noise i.e. low noise
plt.plot(x, signal)
plt.scatter(x, y) #scatter plot

plt.show()