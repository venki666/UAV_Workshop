#enumerateEx.py
class Fruit: 
	def __init__(self, *fruits):
		self.fruits = fruits

	def fruitList(self):
		# 1 is used for starting index as 1
		for i, fruit in enumerate(self.fruits,1): 
			yield(i, fruit)

fruits = Fruit("Apple", "Banana", "Pear")

for fruit in fruits.fruitList():
	print(fruit)
#(1, 'Apple')
#(2, 'Banana')
#(3, 'Pear')