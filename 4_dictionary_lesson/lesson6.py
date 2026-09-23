# Taking student information from the user

name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
course = input("Enter your course: ")
marks = int(input("Enter your marks: "))

# Creating dictionary
student = {
    "name": name,
    "age": age,
    "city": city,
    "course": course,
    "marks": marks
}

print("\nStudent Information")
print(student)


# if, elif, else
if student["marks"] >= 75:
    print("Grade: A")
elif student["marks"] >= 60:
    print("Grade: B")
elif student["marks"] >= 40:
    print("Grade: C")
else:
    print("Grade: Fail")
