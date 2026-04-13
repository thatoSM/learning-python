# My first real Python program - a simple calculator
# Day 3 of my developer journey

print("=== Welcome to my python Calculator ===")
print()

# Ask the user for two numbers
# input() gets the text from the user, float() turns that txt into a number
first_number = float(input("Enter the second number: "))
second_number = float(float(input("Enter the second number: ")))

# Ask what thy want to do
print()
print("What would you like to do?")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
choice = input("Enter 1, 2, 3, or 4: ")

# Do the math based on their choice
if choice == "1" :
    result = first_number + second_number
    print(f"{first_number} + {second_number} = {result}")
elif choice == "2" :
    result = first_number - second_number
    print(f"{first_number} - {second_number} = {result}")
elif choice == "3" :
    result = first_number * second_number
    print(f"{first_number} * {second_number} = {result}")
elif choice == "4" :
    if second_number == 0:
        print("Error: you can't divide by zero!")
    else:
        result = first_number / second_number
        print(f"{first_number} / {second_number} = {result}")
else:
    print("That's not a valid choice. Please run the program again.")

print()
print("Thanks for using the calculator!")