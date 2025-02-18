def calculate_area(length, width):
    # the area of the rectangle
    area = length * width
    return area

# Get user input for length and width
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Call the function and print the result
result = calculate_area(length, width)
print(f"The area of the rectangle is: {result}")