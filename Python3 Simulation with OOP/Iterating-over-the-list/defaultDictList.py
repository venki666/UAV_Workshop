#defaultDictList.py
from collections import defaultdict

flowers = [("Rose", 'White'), ("Lotus", "Red"),
        ("Rose", 'Red'), ("Lily", 'Yellow'),
        ("Rose", 'Yellow'),]

#create default dict
flowerColor = defaultdict(list)

#enter value in dict
for flower, color in flowers:
        flowerColor[flower].append(color)

for flower in flowerColor:
        print(flower, flowerColor[flower])
		# Lily ['Yellow']
		# Rose ['White', 'Red', 'Yellow']
		# Lotus ['Red']