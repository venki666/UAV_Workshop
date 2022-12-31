#tupleEx.py
a = 24, "as it is", "abc", 2+2j

## some times () brackets are used to define tuple as shown below
#a = (24, "as it is", "abc", 2+2j)

# index start with 0 
# i.e. location of number 24 is '0' in the list
print(a[0]) # 24
print(a[2]) # abc

##Following lines will give error,

##as value can be changed in tuple
#a[2]='xyz' # error

##as size of the tuple can not be changed
# a.append(20) # error