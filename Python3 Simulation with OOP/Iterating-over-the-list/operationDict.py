#operationDict.py
fruits = ["Apple", "Banana", "Pear"]
prices = [10, 12, 9]

fruitDict = dict(zip(fruits, prices))

#sort by keys as fruitDict.keys() is used first 
# if fruitDict.values() is used first, then it will be sorted by price
sort_fruit_byName = sorted(zip(fruitDict.keys(), fruitDict.values()))
print("sorted alphabatically with price:", sort_fruit_byName)
#sorted alphabatically with price: [('Apple', 10), ('Banana', 12), ('Pear', 9)]
                         
# min: for finding minimum value as fruitDict.values() is used first
min_price = min(zip(fruitDict.values(), fruitDict.keys()))
print("Cheapest Fruit: ", min_price)
#Cheapest Fruit:  (9, 'Pear')

#see below code as well
max_price = max(fruitDict)
print(max_price)  #Pear i.e. according to letter

max_price = max(fruitDict.values()) 
print(max_price) #12 i.e. maximum price