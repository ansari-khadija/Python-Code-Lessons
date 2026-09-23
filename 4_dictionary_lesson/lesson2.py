# Creating a dictionary
student = {
    "name": "Rahul",
    "age": 20,
    "city": "Malegaon",
    "course": "Python"
}

# 1. keys()
print("Keys:", student.keys())

# 2. values()
print("Values:", student.values())

# 3. items()
print("Items:", student.items())

# 4. get()
print("Name:", student.get("name"))
print("Marks:", student.get("marks", "Not Available"))

# 5. update()
student.update({"age": 21, "marks": 85})
print("After update:", student)

# 6. pop()
student.pop("city")
print("After pop:", student)

# 7. popitem()
student.popitem()
print("After popitem:", student)

# 8. setdefault()
student.setdefault("city", "Pune")
print("After setdefault:", student)

# 9. copy()
new_student = student.copy()
print("Copied dictionary:", new_student)

# 10. clear()
new_student.clear()
print("After clear:", new_student)
