#zipIteration.py
from itertools import zip_longest

fruits = ["Apple", "Banana", "Pear"]
prices = [1, 2, 3, 4, 5]

print(list(zip(fruits, prices)))#[('Apple', 1), ('Banana', 2), ('Pear', 3)]

#zip includes shortest list and add other list to it
for fruit, price in zip(fruits, prices):
	print("%s: $%s" % (fruit, price))
#Apple: $1
#Banana: $2
#Pear: $3

#to add longest list use zip_longest
#by default is store None for undefined items
for fruit, price in zip_longest(fruits, prices):
	print("%s: $%s" % (fruit, price))
#Apple: $1
#Banana: $2
#Pear: $3
#None: $4
#None: $5
 
#use fillvalue to give desire name to unavailble items e.g. 'Free' in below line
for fruit, price in zip_longest(fruits, prices, fillvalue="Free"):
	print("%s: $%s" % (fruit, price))
#Apple: $1
#Banana: $2
#Pear: $3
#Free: $4
#Free: $5