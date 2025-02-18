#WhileExample1.py: Print numbers upto 5
n=1 #initial value of number
print("Numbers upto 5: ")
while n<10:
    print(n, end=" "), #end=" ": to stop row change after print
    n=n+1
    #n+=1 #n = n+1
print("\nCode ended at n =" ,n)