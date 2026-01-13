while True:
    try:
        number1 = float(input("Enter a number: "))
        operation = input("Enter an operation + , - , x , / : ")
        number2 = float(input("Enter another number: "))

        if operation == "+":
            print(f"{number1} + {number2} = {number1 + number2}")
        elif operation == "-":
            print(f"{number1} - {number2} = {number1 - number2}")
        elif operation == "x":
            print(f"{number1} x {number2} = {number1 * number2}")
        elif operation == "/":
            try:
                print(f"{number1} / {number2} = {number1 / number2}")
            except ZeroDivisionError:
                print(f"{number1} / {number2} = Undefined")
        else:
            print("Invalid operation")

        break 

    except ValueError:
        print("Please enter a valid number")
        continue