#fileReadEx2.py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

#load and save column data in variables
# usecols=(1,0): load column-1 first and save to theoryBER;  
# and column-0 to SNR_db
# you can define usecols in any order e.g. usecols(0,2) etc. 
SNR_db, theoryBER = np.loadtxt('bpsk.csv', unpack=True, 
		delimiter=',', 
		skiprows=1, 
		usecols=(1,0,)
	)

# usecols=(2): load column-1 save to randomNumber
#do not skip the command after 2 i.e. usecols=(2,))
NormalrandomNumber = np.loadtxt(
		'bpsk.csv', 
		unpack=True, 
		delimiter=',', 
		skiprows=1, 
		usecols=(2,)
	)

RandomNumber = np.loadtxt(
		'bpsk.csv', 
		unpack=True, 
		delimiter=',', 
		skiprows=1, 
		usecols=(3,)
	)

##Figure 1
plt.semilogy(SNR_db, theoryBER, '--mo')
plt.ylabel('BER')
plt.xlabel('SNR')
plt.title('BPSK BER Curves')
plt.legend(['Theory'], loc='upper right')
plt.grid()

#Figure 2
#plot two different figure in same window, 
#i.e. NormalrandomNumber and RandomNumber
plt.figure() # create new figure window
plt.plot(NormalrandomNumber)
plt.plot(RandomNumber, '--r')
plt.ylabel('Value')
plt.xlabel('Iteration')
plt.title('Normally distributed random numbers')
plt.legend(
	['Normally Distributed Random Numbers', 
	'Uniformlly Distributed Random Numbers'], 
	loc='upper right'
	)

#Display all figures
plt.show()