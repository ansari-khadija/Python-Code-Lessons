# Nested Tuples

# Creating a nested tuple
students = (
    ("Rahul", 20, "Python"),
    ("Amit", 21, "Java"),
    ("Priya", 19, "C++")
)

print("Students:")
print(students)


# Accessing individual nested tuples
print("\n--- Accessing Nested Tuples ---")

print("First student:", students[0])
print("Second student:", students[1])
print("Third student:", students[2])


# Accessing elements inside nested tuples
print("\n--- Accessing Individual Elements ---")

print("First student name:", students[0][0])
print("First student age:", students[0][1])
print("First student course:", students[0][2])

print("Second student name:", students[1][0])
print("Second student course:", students[1][2])


# Slicing nested tuple
print("\n--- Slicing ---")

print("First two students:", students[0:2])


# Creating another nested tuple
print("\n--- Nested Tuple Example ---")

college = (
    ("Python", "Rahul", 85),
    ("Java", "Amit", 78),
    ("C++", "Priya", 92)
)

print("College data:", college)
print("Priya's marks:", college[2][2])