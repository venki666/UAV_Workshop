#fileSaveEx2.py
import numpy as np
from scipy.special import erfc 
from itertools import zip_longest


#BPSK: theoretical error
SNR_db = np.array(np.arange(-2, 10, 1),float)
theoryBER = np.zeros(len(SNR_db),float)
for i in range(len(SNR_db)):
	theoryBER[i] = 0.5*erfc(np.sqrt(10**(SNR_db[i]/10)))

#Random numbers
rn = np.random.randn(100) #Normally Distributed Random Numbers
r = np.random.rand(100) #Uniformly Distributed Random Numbers

#save data in .csv file

#zip_longest is used
#because 'rn' has different length than SNR_db adn theory_BER.
#zip_longest checks the highest length, 
#to create the number of rows in .csv file.
#if 'zip' is used instead of zip_longest, 
#then lowest number of rows will be created in .csv file.
#and we will loose the remaining lines for 'rn' and 'r' in this example.

#mention all data in following line
data  = zip_longest(theoryBER, SNR_db, rn, r, fillvalue=0)
#add header(title) for each data, to recognize the column in .csv file
np.savetxt(
		'bpsk.csv', 
		list(data), 
		fmt = '%f, %f, %f, %f', #%f to store in float format
		header='Theory, SNR, Normal Random Numbers, Uniform Random Number'
	)