#fileReadEx.py: read and plot data from .mat file
import numpy as np
import matplotlib.pyplot as plt

##Figure 1
# SNR_db on x-axis, theoryBER on y-axis
#--mo: plot in magenta color with 'o' marker
plt.semilogy(SNR_db, theoryBER, '--mo') 
plt.ylabel('BER')
plt.xlabel('SNR')
plt.title('BPSK BER Curves')
plt.legend(['Theory'], loc='upper right')
plt.grid()

#Figure 2
#plot two different figure in same window, 
#i.e. NormalrandomNumber and RandomNumber
plt.figure() # open new figure window
plt.plot(rn)
plt.plot(r, '--r') # '--r': plot in red color with broken line
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