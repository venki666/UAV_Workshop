#orderDictEx.py
from collections import OrderedDict

flowerColor = OrderedDict()

flowerColor['Lotus'] = 'Red'
flowerColor['Rose'] = 'Yellow'
flowerColor['Lily'] = 'White'

for flower in flowerColor:
        print(flower, flowerColor[flower])
  		# Lotus Red
		# Rose Yellow
		# Lily White