while True:
    print("\n=== Simple Python Calculator ===")
    
    try:
        print("""
        +. Addition
        -. Subtraction
        *. Multiplication
        /. Divide
        1. Area of Square
        4. Exit
        """)
        operator = input("Enter operator from option: ")
        
        if operator == "1":
            try:
                side = int(input("Enter side of a square : "))
                area = side * side
                print("Area of a square: ", area)
            except ValueError:
                print("Enter right value")
            continue
        elif operator == "4":
            print("Exiting Calculator...")
            break
        
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            try:
                result = num1 / num2
            except ZeroDivisionError:
                print("Error! Cannot divide by zero.")
                continue
        
        else:
            print("Invalid operator! Please try again.")
            continue
        
        print("Result:", result)
    
    except ValueError:
        print("Invalid number input. Please enter numeric values only.")
    
    choice = input("Do you want to calculate again? (yes/no): ").lower()
    if choice != 'yes':
        print("Exiting Calculator...")
        break