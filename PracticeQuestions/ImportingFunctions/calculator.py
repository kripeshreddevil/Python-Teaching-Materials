# calculator.py

# Import specific functions from math_operations
from math_operations import add, subtract, multiply, divide


def main():
    print("Welcome to the Python Calculator!")
    print("Choose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # Get user choice
    choice = int(input("Enter the number of your choice (1-4): "))

    # Ensure valid choice
    if choice not in [1, 2, 3, 4]:
        print("Invalid choice. Exiting.")
        return

    # Get numbers from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform the chosen operation
    if choice == 1:
        print(f"The result is: {add(num1, num2)}")
    elif choice == 2:
        print(f"The result is: {subtract(num1, num2)}")
    elif choice == 3:
        print(f"The result is: {multiply(num1, num2)}")
    elif choice == 4:
        print(f"The result is: {divide(num1, num2)}")


main()
