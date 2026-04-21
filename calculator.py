# Advanced Calculator — Day 13
# Features: continuous running, functions, error handling, history

# This list will store our calculation history
history = []

def get_number(prompt):
    """
     Ask the user for a number. If they type something that isn't a number,
    apologise and ask again. Keeps asking until we get a valid number.
    """
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("That's not a valid number. Please try again.")

def add(a, b):
    """Add two numbers and return the result."""
    return a + b

def subtract(a, b):
    """Subtract b from a and return the result."""
    return a - b

def multiply(a, b):
    """Multiply two numbers and return the result."""
    return a * b

def divide(a, b):
    """Divide the two numbers and return the result"""
    if b == 0:
        return None
    return a / b

def power(a, b):
    """Calculate a to the power b and return the result"""
    return a ** b

def show_history():
    """Print the history of calculations."""
    if len(history) == 0:
        print("No calculations yet.")
    else: 
        print("\n=== History ===")
        for item in history:
            print(item)
        print("================\n")

def show_menu():
    """Display the menu of options."""
    print("\n=== calculator ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. View History")
    print("7. Quit")

# Main program loop
print("Welcome to Advanced Calculator")

while True:
    show_menu()
    choice = input("Choose an option (1-7): ")

    if choice == "7":
        print("Thanks for using the calculator. Goodbye!")
        break

    if choice == "6":
        show_history()
        continue

    if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Invalid choice. Plase pick a numbr from 1 to 7")
        continue

    # Get two numbers from the user
    a = get_number("Enter the first number: ")
    b = get_number("Enter the second number: ")

    # Do th calculation based on choice
    if choice == "1":
        result = add(a, b)
        record = f"{a} + {b} = {result}"
    elif choice == "2":
        result = subtract(a, b)
        record = f"{a} - {b} = {result}"
    elif choice == "3":
        result = multiply(a, b)
        record = f"{a} * {b} = {result}"
    elif choice == "4":
        result = divide(a, b)
        if result is None:
            print("Error: Cannot divide by zero.")
            continue
        record = f"{a} / {b} = {result}"
    elif choice == "5":
        result = power(a, b)
        record = f"{a} ** {b} = {result}"

    print(f"Result: {record}")
    history.append(record)