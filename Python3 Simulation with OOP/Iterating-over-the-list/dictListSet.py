#dictListSet.py
flowerColor = {
     'flower': ["Rose", "Lotus", "Lily"],    #list
     'color': {"Red", "Yellow", "Pink", "White"}     #set
 }

print(flowerColor.items())
#dict_items([('flower', ['Rose', 'Lotus', 'Lily']), 
#   ('color', {'White', 'Yellow', 'Red', 'Pink'})])

print(flowerColor.keys())
#dict_keys(['flower', 'color'])

print(flowerColor.values())
#dict_values([['Rose', 'Lotus', 'Lily'], {'White', 'Yellow', 'Red', 'Pink'}])

flowerColor['flower'][0]
#'Rose'