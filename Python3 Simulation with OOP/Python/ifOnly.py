#ifOnly.py: uses multiple if to check even and odd nubmer

# "input" command takes input as string
# int is used for type conversion
x=int(input('Enter the number:\t')) #\t is used for tab in the output

# % is used to calculate remainder
if x%2==0: 
    print ("Number is even")
if x%2!=0:
    print ("Number is odd")

'''
Output-1st run:
Enter the number:	10
Number is even

Output-2nd run:
Enter the number:	15
Number is odd
'''