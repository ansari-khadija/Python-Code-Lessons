# Create a dictionary
student = {
    "name": "Rahul",
    "age": 20,
    "city": "Malegaon",
    "course": "Python"
}

# Accessing values
print("Name:", student["name"])
print("Age:", student["age"])


# Adding a new item
student["marks"] = 85
print("After adding:", student)


# Updating an item
student["age"] = 21
print("After updating:", student)


# Deleting an item
del student["city"]
print("After deleting:", student)


# Membership operations
print("name" in student)
print("city" in student)

print("name" not in student)
print("city" not in student)


# Dictionary comparison
a = {"x": 1, "y": 2}
b = {"x": 1, "y": 3}

print(a == b)
print(a != b)


# Identity operations
a = {"name": "Rahul"}
b = a

print(a is b)
print(a is not b)


# Dictionary methods
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# Length
print("Length:", len(student))
