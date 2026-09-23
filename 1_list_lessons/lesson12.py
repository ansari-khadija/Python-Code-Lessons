# List Operations
# Create a list

numbers = [10, 20, 30, 40, 50]

# Arithmetic operations

addition = numbers[0] + numbers[1]
subtraction = numbers[2] - numbers[0]
multiplication = numbers[1] * numbers[3]
division = numbers[3] / numbers[0]

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)

# Membership operators

print(20 in numbers)
print(60 in numbers)

print(20 not in numbers)
print(60 not in numbers)

# Comparison

a = [1, 2, 3]
b = [1, 2, 4]

print(a == b)
print(a != b)
print(a < b)
print(a > b)

# Identity

a = [1, 2, 3]
b = a

print(a is b)
print(a is not b)