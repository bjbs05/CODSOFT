# Simple Calculator with basic arithmetic operations

def calculator():
    print("Simple Calculator")
    
    # Input two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Display the operation choices
    print("\nSelect operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    # Input the operation choice
    choice = input("\nEnter your choice (1/2/3/4): ")
    
    # Perform the selected operation
    if choice == '1':
        result = num1 + num2
        print(f"\nThe result of {num1} + {num2} is: {result}")
    elif choice == '2':
        result = num1 - num2
        print(f"\nThe result of {num1} - {num2} is: {result}")
    elif choice == '3':
        result = num1 * num2
        print(f"\nThe result of {num1} * {num2} is: {result}")
    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"\nThe result of {num1} / {num2} is: {result}")
        else:
            print("\nError! Division by zero is not allowed.")
    else:
        print("\nInvalid input! Please select a valid operation.")

# Run the calculator
calculator()
