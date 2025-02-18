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