#fileSaveEx.py
import numpy as np
from scipy.special import erfc 
#BPSK: theoretical error
SNR_db = np.array(np.arange(-2, 10, 1)) #SNR in db
SNR = 10**(SNR_db/10) # SNR_db to SNR conversion

theoryBER = np.zeros(len(SNR_db),float) # zero vector of size SNR_db

for i in range(len(SNR_db)):
	theoryBER[i] = 0.5*erfc(np.sqrt(SNR[i]))

#Random numbers
rn = np.random.randn(100) #Normally Distributed Random Numbers
r = np.random.rand(100) #Uniformly Distributed Random Numbers