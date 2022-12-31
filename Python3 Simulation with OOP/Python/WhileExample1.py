#WhileExample1.py: Print numbers upto 5

n=1 #initial value of number
print("Numbers upto 5: ")
while n<6:
    print(n, end=" "), #end=" ": to stop row change after print
    n=n+1
print("\nCode ended at n =  %s" % n)

'''
output:
Numbers upto 5: 
1 2 3 4 5 
Code ended at n =  6
'''