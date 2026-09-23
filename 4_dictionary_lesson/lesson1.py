# Taking student information from the user
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
course = input("Enter your course: ")


# Creating a dictionary
student = {
    "name": name,
    "age": age,
    "city": city,
    "course": course
}


# Display dictionary
print("Student Information")
print(student)
print(type(student))


# Accessing dictionary values
print("Name:", student["name"])
print("Age:", student["age"])
print("City:", student["city"])
print("Course:", student["course"])


# Membership operators
print("name" in student)
print("marks" in student)

print("name" not in student)
print("marks" not in student)


# Adding a new item
student["marks"] = 85
print("After adding marks:", student)


# Updating a value
student["age"] = 21
print("After updating age:", student)


# Removing an item
student.pop("city")
print("After removing city:", student)


# Dictionary properties / methods
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())


# Length of dictionary
print("Number of items:", len(student))
