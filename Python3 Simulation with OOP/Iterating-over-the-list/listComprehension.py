#listComprehension.py
num = [1, 2, 3, 4, 5]

#square all the numbers in list 'num'
square_num = [n**2 for n in num]
print(square_num) #[1, 4, 9, 16, 25]

#squre only even number
square_even_num = [n**2 for n in num if n%2==0]
print(square_even_num)#[4, 16]