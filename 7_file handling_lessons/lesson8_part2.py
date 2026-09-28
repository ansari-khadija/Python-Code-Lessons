try:
    a = int(input("enter number1: "))
    b = int(input("enter number2: "))
    print(a / b)

except (ZeroDivisionError, ValueError) as msg:
    print("provide valid input only and error is:", msg)

except Exception as msg:
    print("unknown error occurred:", msg)

finally:
    print("finally!")
