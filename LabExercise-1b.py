# question-4
# Given lists
ListColour = ["Black", "Red", "Maroon", "Yellow"]
ListCode = ["000000", "FF0000", "800000", "FFFF00"]
print("\nQuestion-4")
# Initialize an empty list to hold the dictionaries
list_of_dicts = []
# Iterate over both lists simultaneously using zip
for color, code in zip(ListColour, ListCode):
    # Create a dictionary for each pair of color and code
    color_dict = {"colorName": color, "colorCode": code}
    # Append the dictionary to the list
    list_of_dicts.append(color_dict)
# Print 
print(list_of_dicts)



# question-5
def even_numbers_and_squares(start, end):
    # Iterate through the given range
    for number in range(start, end):
        # Check if the number is even
        if number % 2 == 0:
            # Print the even number and its square
            print(f"Number: {number}, Square: {number**2}")
# (a) Range 1 to 50

print("\nQuestion-5")
print("\nEven numbers and their squares in the range 1 to 50:")
even_numbers_and_squares(1, 50)

print("\n")
# (b) Range 1 to 100
print("Even numbers and their squares in the range 1 to 100:")
even_numbers_and_squares(1, 100)



# question-6
def sum_of_digits(number):
    # Convert the number to a string to iterate over each digit
    digits = str(number)
    # Calculate the sum of the digits
    total = sum(int(digit) for digit in digits)
    return total 
def reverse_number(number):
    # Convert the number to a string, reverse it, and convert it back to an integer
    reversed_number = int(str(number)[::-1])
    return reversed_number 
# Read a four-digit number from the user
print("\nQuestion-6")
number = int(input("Enter a four-digit number: "))
# Ensure the number is four digits
if 1000 <= number <= 9999:
    # Calculate and print the sum of digits
    sum_digits = sum_of_digits(number)
    print(f"Sum of digits: {sum_digits}")
    # Calculate and print the reverse of the number
    reversed_num = reverse_number(number)
    print(f"Reversed number: {reversed_num}")
else:
    print("Please enter a valid four-digit number.")




