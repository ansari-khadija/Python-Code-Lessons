# Dictionary Packing

name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
course = input("Enter your course: ")

student = {
    "name": name,
    "age": age,
    "city": city,
    "course": course
}

print(student)


# Dictionary Unpacking
print("\n--- Dictionary Unpacking ---")

name = student["name"]
age = student["age"]
city = student["city"]
course = student["course"]

print("Name:", name)
print("Age:", age)
print("City:", city)
print("Course:", course)


# Dictionary Keys Unpacking
print("\n--- Keys Unpacking ---")

name, age, city, course = student.keys()

print("Name:", name)
print("Age:", age)
print("City:", city)
print("Course:", course)


# Dictionary Values Unpacking
print("\n--- Values Unpacking ---")

name, age, city, course = student.values()

print("Name:", name)
print("Age:", age)
print("City:", city)
print("Course:", course)


# Dictionary Items Unpacking
print("\n--- Items Unpacking ---")

for key, value in student.items():
    print(key, "=", value)
