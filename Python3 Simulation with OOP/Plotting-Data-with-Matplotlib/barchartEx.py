#barchartEx.py
import matplotlib.pyplot as plt

plt.close("all")

x = [1, 2, 4]
years = [1999, 2014, 2030]

plt.bar(years, x)

plt.show()