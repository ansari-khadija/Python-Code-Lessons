# List Packing and Unpacking

# List Packing
print("--- List Packing ---")

name= input("enter your name:")
age= int(input("enter your age:"))
city= input("enter your city:")
course= input("enter your course:")

student = [name, age, city, course]

print("Student list:", student)


# List Unpacking string
print("\n--- List Unpacking ---")

name, age, city, course = student

print("Name:", name)
print("Age:", age)
print("City:", city)
print("Course:", course)

print(student)


# Unpacking numbers
print("\n--- Unpacking Numbers ---")

numbers = (10, 20, 30, 40, 50)

a, b, c, d, e = numbers

print("a =", a)
print("b =", b)
print("c =", c)
print("d =", d)
print("e =", e)


# Extended unpacking
print("\n--- Extended Unpacking ---")

numbers = (10, 20, 30, 40, 50)

first, * middle, last = numbers

print("First:", first)
print("Middle:", middle)
print("Last:", last)