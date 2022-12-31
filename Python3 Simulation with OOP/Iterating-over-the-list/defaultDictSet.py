#defaultDictSet.py
from collections import defaultdict

flowers = [("Rose", 'White'), ("Lotus", "Red"),
        ("Rose", 'Red'), ("Lily", 'Yellow'),
        ("Rose", 'Yellow'),]

#create default dict
flowerColor = defaultdict(set)

#enter value in dict
for flower, color in flowers:
        flowerColor[flower].add(color)

for flower in flowerColor:
        print(flower, flowerColor[flower])
  		# Lily {'Yellow'}
		# Lotus {'Red'}
		# Rose {'Yellow', 'White', 'Red'}