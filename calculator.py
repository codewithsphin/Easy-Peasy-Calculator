# Python program to create Easy-Peasy calculator 

# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract second number from first
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide first number by second
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"  # Prevent division by zero
    return a / b

# --- Main program with loop ---
while True:
    # Show welcome message and options
    print("\nWelcome to the Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    # Get user choice
    choice = input("Enter choice (1/2/3/4/5): ")

    # Exit the program
    if choice == '5':
        print("Thanks for using the Easy-Peasy calculator. Goodbye!")
        break  # Exit the loop

    # Check if valid operation
    if choice in ['1', '2', '3', '4']:
        # Get numbers from user
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue  # Restart loop if input is not a number

        # Perform the selected operation
        if choice == '1':
            print("Result:", add(num1, num2))  # Call add() function
        elif choice == '2':
            print("Result:", subtract(num1, num2))  # Call subtract() function
        elif choice == '3':
            print("Result:", multiply(num1, num2))  # Call multiply() function
        elif choice == '4':
            print("Result:", divide(num1, num2))  # Call divide() function
    else:
        print("Invalid choice! Please enter a number from 1 to 5.")
