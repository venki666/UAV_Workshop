#dictEx.py
myDict = {} 		# define new dictionary
myDict[1] = "one"  # 1 is called key; "one" is called value
myDict['a'] = "alphabet"

print(myDict) 		     # {1: 'one', 'a': 'alphabet'}
print(myDict.items())  # dict_items([(1, 'one'), ('a', 'alphabet')])
print(myDict.keys())   # dict_keys([1, 'a'])
print(myDict.values()) # dict_values(['one', 'alphabet'])

print(myDict[1]) #one
print(myDict['a']) # alphabet

# add key-value while creating the dictionary
subjectDict = {'py': 'Python', 'np': 'Numpy', 'sp':'Scipy'}
print(subjectDict) # {'py': 'Python', 'sp': 'Scipy', 'np': 'Numpy'}