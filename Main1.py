while True:
    try:
        numerator=int(input("Enter the numerator: "))
        denominator=int(input("Enter the denominator: "))
        answer=numerator/denominator
        print(f"{numerator}/{denominator} = {answer}")
        break
    except ZeroDivisionError:
        print("Please enter a number other than 0")
        continue
    except ValueError:
        print("Please enter a digit")
        continue

    