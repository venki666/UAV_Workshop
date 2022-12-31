#mapFilterEx.py
num = [1, 2, 3, 4, 5]

#square all the number in list 'num' using map
m = map(lambda n: n**2, num)
print(m) # <map object at 0x000000000AE77EF0>
square_num = list(m) #convert 'm' into list
print(square_num) #[1, 4, 9, 16, 25]

n = list(map(lambda n: n**3, num))  #list used with map in one line
print(n) #[1, 8, 27, 64, 125]

#square only even number in list 'num' using map and filter
e = map(lambda n: n**2, filter(lambda n: n % 2 == 0, num))
square_even_num = list(e)
print(square_even_num) #[4, 16]