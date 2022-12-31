#pieEx.py
import matplotlib.pyplot as plt

plt.close("all")

x = [30, 20, 15, 25, 10]
dataName = ['data1', 'data2', 'data3', 'data4', 'data5']

plt.figure(figsize=(5,5)) #figsize: output figure window size
plt.pie(x, labels=dataName)

plt.show()