# Create a set
numbers = {10, 20, 30, 40, 50}

# Arithmetic operations
addition = 10 + 20
subtraction = 30 - 10
multiplication = 20 * 40
division = 40 / 10

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
a = {1, 2, 3}
b = {1, 2, 4}

print(a == b)
print(a != b)

# Set comparison
print(a < b)   # Proper subset
print(a > b)   # Proper superset


# Identity
a = {1, 2, 3}
b = a

print(a is b)
print(a is not b)
