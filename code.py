# Define a function to perform addition
def add(x, y):
    return x + y

# Define a function to perform subtraction
def subtract(x, y):
    return x - y

# Define a function to perform multiplication
def multiply(x, y):
    return x * y

# Define a function to perform division
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Main calculator loop
while True:
    # Display menu
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'quit' to end the program")

    # Take user input
    user_input = input(": ")

    # Check for the user's choice
    if user_input == "quit":
        break
    elif user_input in ("add", "subtract", "multiply", "divide"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if user_input == "add":
            print("Result: " + str(add(num1, num2))
        elif user_input == "subtract":
            print("Result: " + str(subtract(num1, num2))
        elif user_input == "multiply":
            print("Result: " + str(multiply(num1, num2))
        elif user_input == "divide":
            print("Result: " + str(divide(num1, num2))
    else:
        print("Invalid input. Please try again.")
