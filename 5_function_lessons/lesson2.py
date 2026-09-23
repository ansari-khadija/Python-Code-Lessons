# funtion with user input
def student_info():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    course = input("Enter your course: ")

    print("\nStudent Information")
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)

student_info()
