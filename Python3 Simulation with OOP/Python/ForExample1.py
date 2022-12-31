#ForExample1.py: Print numbers 1-5

print("Numbers in forward order")
for i in range(5):
    print(i+1, end=" ")
print("\nFinal value of i is: ", i)

print ("\nNumbers in reverse order")
for j  in range(5, 0, -1):
    print(j, end=" "), 
print("\nFinal value of i is: ", j)

'''
outputs:
Numbers in forward order
1 2 3 4 5 
Final value of i is:  4

Numbers in reverse order
5 4 3 2 1 
Final value of i is:  1
'''

fruits=["apple", "banana", "orange"]
print("List of fruits are shown below:")
for i in fruits:
    print(i)
'''
List of fruits are shown below:
apple
banana
orange
'''