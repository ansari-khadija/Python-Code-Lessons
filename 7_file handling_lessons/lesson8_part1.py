try:
    x=int(input("Enter number1:"))
    y=int(input("Enter number2:"))
    print(x/y)
except(ZeroDivisionError,ValueError)as msg:
    print("provide valid input only and error is:",msg)
except:
    print("unknown error occured ")