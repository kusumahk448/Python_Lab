# question-7
import math

def calculate_area(a, b, c):
    # Calculate the semi-perimeter
    s = (a + b + c) / 2
    # Calculate the area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area
# Read the sides of the first triangle from the user
print("\nQuestion-7")
a1 = float(input("Enter the first side of the first triangle: "))
b1 = float(input("Enter the second side of the first triangle: "))
c1 = float(input("Enter the third side of the first triangle: "))
# Read the sides of the second triangle from the user
a2 = float(input("Enter the first side of the second triangle: "))
b2 = float(input("Enter the second side of the second triangle: "))
c2 = float(input("Enter the third side of the second triangle: "))
# Calculate the areas of both triangles
area1 = calculate_area(a1, b1, c1)
area2 = calculate_area(a2, b2, c2)
# Calculate the total area
total_area = area1 + area2
# Calculate the percentage contribution of each triangle
percentage1 = (area1 / total_area) * 100
percentage2 = (area2 / total_area) * 100
# Print the output
print(f"\nThe area of the first triangle is: {area1:.2f}")
print(f"The area of the second triangle is: {area2:.2f}")
print(f"The total area enclosed by both triangles is: {total_area:.2f}")
print(f"The first triangle contributes {percentage1:.2f}% to the total area.")
print(f"The second triangle contributes {percentage2:.2f}% to the total area.")


# question-8
# List of dictionaries containing information about people
people = [
    {"name": "john doe", "age": 30, "blood_group": "A+"},
    {"name": "jane smith", "age": 25, "blood_group": "B-"},
    {"name": "Emily Davis", "age": 40, "blood_group": "O+"},
    {"name": "Michael Brown", "age": 35, "blood_group": "AB-"},
    {"name": "William Johnson", "age": 28, "blood_group": "A-"},
    {"name": "Emma Wilson", "age": 22, "blood_group": "B+"},
    {"name": "Oliver Martinez", "age": 33, "blood_group": "O-"},
    {"name": "Sophia Anderson", "age": 27, "blood_group": "AB+"},
    {"name": "James Thomas", "age": 45, "blood_group": "A+"},
    {"name": "Isabella Lee", "age": 38, "blood_group": "B-"}
]
print("\nQuestion-8")
# Iterate over each person in the list
for person in people:
    # Print person's details
    print(f"Name: {person['name']}")
    print(f"Age: {person['age']}")
    print(f"Blood Group: {person['blood_group']}")
    # Print a line of dashes to separate each person's information
    print("-" * 25)


# question-9
# Define a tuple of strings
tuple_of_strings = ("apple", "banana", "cherry", "date", "elderberry")
print("\nQuestion-9")
# Extract and print the last character of each string in the tuple
print("Rear elements of each string in the tuple:")
for string in tuple_of_strings:
    # Get the last character of the string
    rear_element = string[-1]
    print(f"String: {string}, Rear element: {rear_element}")


# question-10
def days_in_month(month, year):
    # List of months with their corresponding number of days (non-leap year)
    months_days = {
        "January": 31,
        "February": 28,  # Default for non-leap years
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31
    }
    
    # Check if it's a leap year and adjust February's days
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        months_days["February"] = 29
    
    # Return the number of days for the given month
    return months_days.get(month, "Invalid month")

# Read the month from the user
print("\nQuestion-10")
month = input("Enter the name of the month: ").capitalize()

# If the month is February, ask for the year
if month == "February":
    year = int(input("Enter the year: "))
else:
    # Default year value (not used for non-February months)
    year = 0

# Get the number of days in the month
days = days_in_month(month, year)

# Print the result
if days == "Invalid month":
    print(days)
else:
    print(f"The number of days in {month} is: {days}")

