# modules with function
# funtion with all built in
import math
import random
import datetime

def information(number):

    print("Number:", number)
    print("Square Root:", math.sqrt(number))
    print("Random Number:", random.randint(1, 10))
    print("Date:", datetime.date.today())


number = int(input("Enter a number: "))

information(number)


