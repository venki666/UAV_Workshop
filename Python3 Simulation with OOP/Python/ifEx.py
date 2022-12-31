#ifEx.py
x = 2
# brackets are not necessary (used for clarity of the code)
if (x%2 == 0): # % sign gives the value of the remainder e.g. 5%3 = 2
	#if above condition is true, only then following line will execute
	print('Number is even.')

#this line will execute always as it is not inside 'if'
print('Bye Bye')

'''
Number is even.
Bye Bye
'''

'''
if you put x = 3, then output will be,
Bye Bye
i.e. Number is even will not be printed as 'if' condition is not satisfied.
'''