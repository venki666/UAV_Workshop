#listEx.py
a = [24, "as it is", "abc", 2+2j]
# index start with 0 
# i.e. location of number 24 is '0' in the list
print(a[0]) # 24
print(a[2]) # abc

#replace 'abc' with 'xyz'
a[2]='xyz'
print(a[2]) # xyz

# Add 20 at the end of list
a.append(20)
print(a) # [24, 'as it is', 'abc', (2+2j), 20]