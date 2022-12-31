#scipyEx.py
import numpy as np
#import LU factorization command from scipy.linalg
from scipy.linalg import lu 

#define matrix 'a'
a= np.mat('1, 1, 1; 3, 4, 6; 2, 5, 4') # define matrix

# perform LU factorization and 
# save the values in p, l and u as it returns 3 values
[p, l, u]= lu(a) 

#print values of p, l and u
print("p = ", p) 
print("l = ", l)
print("u = ", np.round(l,2))


print("Type of P: ", type(p)) #type of p: ndarray
#p*l*u will give wrong results 
# because types are not matrix (but ndarray) as shown above
r = p.dot(l).dot(u)
print("r = ", r)

#for p*l*u we need to change the ndarray to matrix type as below,  
print("Type of P after np.mat: ", type(np.mat(p)))
m = np.mat(p)*np.mat(l)*np.mat(u)
print("m = ", m)

'''
Outputs: 

p =  [[ 0.  0.  1.]
 [ 1.  0.  0.]
 [ 0.  1.  0.]]

l =  [[ 1.          0.          0.        ]
 [ 0.66666667  1.          0.        ]
 [ 0.33333333 -0.14285714  1.        ]]

u =  [[ 1.    0.    0.  ]
 [ 0.67  1.    0.  ]
 [ 0.33 -0.14  1.  ]]

Type of P:  <class 'numpy.ndarray'>

r =  [[ 1.  1.  1.]
 [ 3.  4.  6.]
 [ 2.  5.  4.]]

Type of P after np.mat:  <class 'numpy.matrixlib.defmatrix.matrix'>

m =  [[ 1.  1.  1.]
 [ 3.  4.  6.]
 [ 2.  5.  4.]]
'''