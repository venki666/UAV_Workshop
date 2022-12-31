#pieEx2.py
import matplotlib.pyplot as plt

plt.close("all")

x = [10, 10, 20, 20, 30]
dataName = ['data1', 'data2', 'data3', 'data4', 'data5']
explode = [0.01, 0, 0, 0.04, 0.09] 

plt.figure(figsize=(5,5))
# autopct='%.2f %%': %.2f display value upto 2 decimal, 
# %% is used for displaying % at the end
plt.pie(x, explode=explode, labels=dataName, autopct='%.2f%%') 
plt.show()