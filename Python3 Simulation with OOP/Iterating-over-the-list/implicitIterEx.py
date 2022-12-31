#implicitIterEx.py
class Fruit: 
	def __init__(self, *fruits):
		self.fruits = fruits

	def __iter__(self):
		return iter(self.fruits)

f = ["Apple", "Banana", "Pear"]
fruits = Fruit(*f)  # *f send list items as 3-arguments.
# above line can be written as below as well.
# fruits = Fruit("Apple", "Banana", "Pear")

#this line is different from above two methods
#fruits =Fruit(f) #it will send fruites as 1-list

i=1 
#iterating over instance of Fruit class. 
for fruit in fruits: # __iter__ will be invoked, as iteration is applied to instance
	print("%s: %s" % (i, fruit))
	i+=1
#1: Apple
#2: Banana
#3: Pear