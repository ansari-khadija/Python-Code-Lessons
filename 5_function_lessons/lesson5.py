# function with built in module
# math module
import math

def calculate(number):
    print("Square Root:", math.sqrt(number))
    print("Power:", math.pow(number, 2))
    print("Factorial:", math.factorial(number))


number = int(input("Enter a number: "))

calculate(number)

# random module
import random

def random_number():
    number = random.randint(1, 100)
    print("Random Number:", number)


random_number()

# statistic module
import statistics

def calculate_marks(marks):
    print("Mean:", statistics.mean(marks))
    print("Median:", statistics.median(marks))
    print("Maximum:", max(marks))
    print("Minimum:", min(marks))


marks = list(map(int, input("Enter marks: ").split()))

calculate_marks(marks)

# date time module
import statistics

def calculate_marks(marks):
    print("Mean:", statistics.mean(marks))
    print("Median:", statistics.median(marks))
    print("Maximum:", max(marks))
    print("Minimum:", min(marks))


marks = list(map(int, input("Enter marks: ").split()))

calculate_marks(marks)


