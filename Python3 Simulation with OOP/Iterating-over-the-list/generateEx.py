#generateEx.py
class Fruit: 
	def __init__(self, *fruits):
		self.fruits = fruits

	def fruitList(self):
		for fruit in self.fruits:
			yield(fruit)

fruits = Fruit("Apple", "Banana", "Pear")

for fruit in fruits.fruitList():
	print(fruit)
#Apple
#Banana
#Pear