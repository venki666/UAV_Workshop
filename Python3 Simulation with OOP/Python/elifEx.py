#elif.py: checks divisibility with 2 and 3

# "int(input())" command takes input as number
x=int(input('Enter the number:\t'))

# % is used to calculate remainder
if x%2==0: #check divisibility with 2
    if x%3==0: # if x%2=0, then check this line
        print("Number is divisible by 2 and 3")
    else:
        print("Number is divisible by 2 only")
        print("x%3= ", x%3)
elif x%3==0: #check this if x%2 is not zero
    print("Number is divisible by 3 only")
else: 
    print("Number is not divisible by 2 and 3")
    print("x%2= ", x%2)
    print("x%3= ", x%3)
print("Thank you")

'''
output 1:
Enter the number:	12
Number is divisible by 2 and 3
Thank you

output 2:
Enter the number:	8
Number is divisible by 2 only
x%3=  2
Thank you

output 3:
Enter the number:	7
Number is not divisible by 2 and 3
x%2=  1
x%3=  1
Thank you

output 4:
Enter the number:	15
Number is divisible by 3 only
Thank you
'''