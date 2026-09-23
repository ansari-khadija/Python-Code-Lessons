# function with operations

# Function for arithmetic operations

def calculator(a, b):

    # Addition
    addition = a + b
    print("Addition:", addition)

    # Subtraction
    subtraction = a - b
    print("Subtraction:", subtraction)

    # Multiplication
    multiplication = a * b
    print("Multiplication:", multiplication)

    # Division
    division = a / b
    print("Division:", division)

    # Floor Division
    floor_division = a // b
    print("Floor Division:", floor_division)

    # Modulus
    modulus = a % b
    print("Modulus:", modulus)

    # Power
    power = a ** b
    print("Power:", power)


# Function call
a, b = map(int, input("Enter a and b: ").split())

calculator(a, b)
