#ifelse1.py: use if-else to check even and odd nubmer

# "input" command takes input as string
x= int(input('Enter the number:\t'))

# % is used to calculate remainder
if x%2==0: 
    print("Number is even")
else:
    print("Number is odd")

'''
Output-1st run:
Enter the number:	10
Number is even

Output-2nd run:
Enter the number:	15
Number is odd
'''