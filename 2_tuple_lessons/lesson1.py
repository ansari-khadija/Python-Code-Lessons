# Taking student information from the user

name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
course = input("Enter your course: ")

# Creating a tuple
student = (name, age, city, course)

print("\n--- Student Information ---")
print(student)

print("\n--- properties of tuple ---")

# 1. Ordered
print("\n--- Ordered Property ---")
print("First element:", student[0])
print("Second element:", student[1])
print("Third element:", student[2])
print("Fourth element:", student[3])

# 2. Different data types
print("\n--- Different Data Types ---")
print("Name:", student[0], "| Type:", type(student[0]))
print("Age:", student[1], "| Type:", type(student[1]))
print("City:", student[2], "| Type:", type(student[2]))
print("Course:", student[3], "| Type:", type(student[3]))

# 3. Duplicate values are allowed
print("\n--- Duplicate Values ---")
subjects = ("Python", "Java", "Python", "C++")
print("Subjects:", subjects)
print("Python appears:", subjects.count("Python"), "times")

# 4. Indexing
print("\n--- Indexing ---")
print("Student Name:", student[0])
print("Student Course:", student[3])

# 5. Slicing
print("\n--- Slicing ---")
print("Name and Age:", student[0:2])
print("City and Course:", student[2:4])

# 6. Immutability
print("\n--- Immutability ---")

'''#try and see the result with this two first then without this 2 line
student[1] = 22
print("Tuple is immutable. Its elements cannot be changed.")
print("Original tuple:", student)'''