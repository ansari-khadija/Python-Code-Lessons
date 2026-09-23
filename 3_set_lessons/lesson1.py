# Taking student information from the user
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
course = input("Enter your course: ")

 # Creating a set

student = {name, age, city, course}

print("Student Information")
print(student)

print("Properties of Set ")

 # 1. Unordered

print(" 1. Unordered Property")
print("Set:", student)
print("Sets do not have a fixed order.")

 # 2. Different data types

print(" 2. Different Data Types")
for item in student:
   print(item, " Type:", type(item))

 # 3. Duplicate values are not allowed

print("3. Duplicate Values")
subjects = {"Python", "Java", "Python", "C++"}
print("Subjects:", subjects)
print("Number of subjects:", len(subjects))

 # 4. Indexing is not supported

print("4. Indexing ")
print("Sets do not support indexing.")

 # 5. Slicing is not supported

print("5. Slicing ")
print("Sets do not support slicing.")

 # 6. Mutability

print(" 6. Mutability ")

student.add("Mumbai")

print("Set is mutable. Elements can be added or removed.")
print("Modified set:", student)