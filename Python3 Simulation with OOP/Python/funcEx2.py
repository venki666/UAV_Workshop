#funcEx2.py: default argument can be defined only after non-default argument
# e.g. addTwoNum(num1=2, num2): is wrong. b must have some defined value
def addTwoNum(num1, num2=2):
	return(num1+num2)

result1 = addTwoNum(3)
print("result1=%s" % result1)

result2 = addTwoNum(3,4)
print("result2=%s" % result2)

'''
result1=5
result2=7
'''
