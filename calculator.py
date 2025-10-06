#!/usr/bin/env python3
"""
Simple Calculator Application
Currently supports: Addition, Subtraction, and Multiplication
"""

def add(a, b):
    """Add two numbers together"""
    return a + b
def subtract(a, b):
    """Subtract two numbers"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b


def main():
    """Main calculator interface"""
    print("=" * 40)
    print("  SIMPLE CALCULATOR")
    print("=" * 40)
    print()
    print("Available operations:")
    print("  [1] Add")
    print("  [2] Subtract")
    print("  [3] Multiply")
    print("  [4] Divide (Coming soon)")
    print("  [0] Exit")
    print()

    while True:
        try:
            choice = input("Select operation: ")

            if choice == '0':
                print("Goodbye!")
                break

            if choice == '1':
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                result = add(num1, num2)
                print(f"\nResult: {num1} + {num2} = {result}\n")
            
            if choice == '2':
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                result = subtract(num1, num2)
                print(f"\nResult: {num1} - {num2} = {result}\n")

            if choice == '3':
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                result = multiply(num1, num2)
                print(f"\nResult: {num1} × {num2} = {result}\n")

            elif choice == '4':
                print("This operation is not yet implemented!\n")

            else:
                print("Invalid choice. Please try again.\n")

        except ValueError:
            print("Invalid input. Please enter valid numbers.\n")
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break


if __name__ == "__main__":
    main()
