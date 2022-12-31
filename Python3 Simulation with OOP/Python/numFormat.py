#numFormat.py
a = 11 #integer
print(hex(a)) #0xb

b = 3.2 # float(decimal)
## print(oct(b)) # error: can't convert float to oct or hex.
# integer can be converted, therefore first convert float to int 
# and then to hex/oct
print(oct(int(b))) #0o3

d = 0X1A # hexadecimal: '0X' is used before number i.e. 1A
print(d) # 26

#add hex and float
print(b+d) #29.2

c = 0o17 # octal: '0o' is used before number i.e. 17
# print command shows the integer value
print(c) # 15
#to see octal form use `oct'
print(oct(c)) #0o17

e = 3+2j # imagenary
print(e) #(3+2j)
print(abs(e)) #3.6055512754639896
# round above value upto 2 decimal
r=round(abs(e),2) 
print(r) #3.61