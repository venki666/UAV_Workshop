#manualIterEx.py
fruits = ["Apple", "Banana", "Pear"]

fruit = iter(fruits)  #start iteration
## above line can be written as follows, 
## fruit = fruits.__iter__()

print(next(fruit)) # Apple
# above line can be written as follows, 
print(fruit.__next__())# Banana
print(next(fruit)) # Pear

##error because list contain only 3 fruits
#print(next(fruit))