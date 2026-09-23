# function with if else elif statement
def check_numbers(numbers):

    for number in numbers:

        if number > 0:
            print(number, "is Positive")

        elif number < 0:
            print(number, "is Negative")

        else:
            print(number, "is Zero")


# Input
numbers = list(map(int, input("Enter numbers: ").split()))

# Function call
check_numbers(numbers)
