# class method in oop methods

class student:
    def __init__(self):
        self.name=input("Enter student name:")
        self.age=int(input("Enter student age:"))
        self.subject=input("Enter Subject:")
        self.marks=int(input("Enter marks:"))

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Subject:", self.subject)
        print("Marks:", self.marks)

        
s1 = student()

s1.display()

# OR another way is to print

# s1 = student()
# print({
#     "Student name:":s1.name,
#     "Student Age:":s1.age,
#     "Student Subject:":s1.subject,
#     "Student Marks:":s1.marks
# })

