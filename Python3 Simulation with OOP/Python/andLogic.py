#andLogic.py: check divisibility with 2 and 3
x=int(input('Enter the number:\t'))

if x%2==0 and x%3==0: #check divisibility with both 2 and 3
    print("Number is divisible by 2 and 3")
elif x%2==0: #check this if x%2 is not zero
    print("Number is divisible by 2 only")    
elif x%3==0: #check this if x%3 is not zero
    print("Number is divisible by 3 only")   
else: 
    print("Number is not divisible by 2 and 3")
    print("x%2= ", x%2)
    print("x%3= ", x%3)
print("Thank you")