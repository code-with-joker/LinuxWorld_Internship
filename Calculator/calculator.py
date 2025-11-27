while True:
    print("\n------- Python Calculator ---------")
    
    print("""
    +  Addition
    -  Subtraction
    *  Multiplication
    /  Division
    
    1. Area of Square
    2. Temperature Conversion
       a. Celsius to Fahrenheit
       b. Fahrenheit to Celsius
          
    3. Weight Conversion
       a. KG to Gram
       b. Gram to KG
    
    4. Exit
    """)

    operator = input("Choose an option: ").lower()

    # AREA OF SQUARE
    if operator == "1":
        try:
            side = float(input("Enter side of a square: "))
            print("Area of square:", side * side)
        except ValueError:
            print("Invalid input")
        continue

    # TEMPERATURE CONVERSION
    elif operator == "2":
        sub = input("Choose (a) C→F or (b) F→C: ").lower()

        try:
            temp = float(input("Enter temperature value: "))

            if sub == "a":
                result = (temp * 9/5) + 32
                print(f"{temp}°C = {result}°F")

            elif sub == "b":
                result = (temp - 32) * 5/9
                print(f"{temp}°F = {result}°C")

            else:
                print("Invalid option")

        except ValueError:
            print("Enter a valid number")
        continue

    # WEIGHT CONVERSION
    elif operator == "3":
        sub = input("Choose (a) KG→Gram or (b) Gram→KG: ").lower()

        try:
            weight = float(input("Enter weight value: "))

            if sub == "a":
                result = weight * 1000
                print(f"{weight} KG = {result} Gram")

            elif sub == "b":
                result = weight / 1000
                print(f"{weight} Gram = {result} KG")

            else:
                print("Invalid option")

        except ValueError:
            print("Enter a valid number")
        continue

    # EXIT
    elif operator == "4":
        print("Exiting calculator...")
        break

    # ARITHMETIC OPERATIONS
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Please enter numeric values only.")
        continue

    if operator == '+':
        print("Result:", num1 + num2)
    elif operator == '-':
        print("Result:", num1 - num2)
    elif operator == '*':
        print("Result:", num1 * num2)
    elif operator == '/':
        try:
            print("Result:", num1 / num2)
        except ZeroDivisionError:
            print("Cannot divide by zero.")
    else:
        print("Invalid operator!")

    # CONTINUE?
    again = input("Do you want to calculate again? (yes/no): ").lower()
    if again != "yes":
        print("Exiting calculator...")
        break
