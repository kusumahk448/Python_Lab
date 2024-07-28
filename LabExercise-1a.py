#question-1
def question1():
    numbers = [12, 34, 64, 57, 87, 90, 11, 23]
    
    while True:
        print("\nMenu:")
        print("1. Display the list")
        print("2. Sum of all items in the list")
        print("3. Product of all items in the list")
        print("4. Largest item in the list")
        print("5. Smallest item in the list")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            print("The given list is:", numbers)
        
        elif choice == '2':
            # Sum of all items
            total_sum = sum(numbers)
            print("Sum of all items of the list is:", total_sum)
            
        elif choice == '3':
            # Product of all items
            product = 1
            for num in numbers:
                product *= num
            print("Product of all items of the list using for loop: ", product)
        
        elif choice == '4':
            # Largest item
            largest = max(numbers)
            print("The largest number from the list is:", largest)
        
        elif choice == '5':
            # Smallest item
            smallest = min(numbers)
            print("The smallest number from the list is:", smallest)
        
        elif choice == '6':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

# Run the menu-driven program
question1()

#question-2
A = ['abc', 'xyz', 'aba', '1221','23342']
print("\nQuestion-2: ")
# Iterate over the list with index
for index, string in enumerate(A):
    # Check if the first and last characters are the same
    if string[0] == string[-1]:
        print(f"Index: {index}, String: {string}")

#question-3-a
n = 5
alph = 65
print("\nQuestion-3")
print("Printing Alphabet pyramid: ")
for i in range(0, n):
    print(" " * (n-i), end=" ")
    for j in range(0, i+1):
        print(chr(alph), end=" ")
        alph += 1
    alph = 65
    print()
#question-3-b
print("\n Printing half pyramid:")
def half_pyramid(n):
    if n > 0:
        # Call the function recursively with a smaller value of n
        half_pyramid(n - 1)
        
        # Print '*' characters for the current row
        print('*' * n)

# Get the number of rows from the user
rows = int(input("Enter the number of rows for the half pyramid: "))

# Call the function to print the half pyramid pattern
half_pyramid(rows)



