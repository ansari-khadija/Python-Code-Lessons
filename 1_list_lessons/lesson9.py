# List with Loops

subjects = ["Python", "Java", "C++", "SQL", "HTML"]

print("Subjects:", subjects)

# 1. Iterating through a lists
print("\n--- Using for Loop ---")

for subject in subjects:
    print(subject)


# 2. Printing with index
print("\n--- Using Index with Loop ---")

for i in range(len(subjects)):
    print("Index", i, ":", subjects[i])


# 3. lists of numbers
print("\n--- Numbers in Tuple ---")

numbers = (10, 20, 30, 40, 50)

total = 0

for number in numbers:
    total = total + number

print("Numbers:", numbers)
print("Total:", total)


# 4. Nested list with loop
print("\n--- Student Records ---")

students = [
    ("Rahul", 20, "Python"),
    ("Amit", 21, "Java"),
    ("Priya", 19, "C++")]


for student in students:
    print("Name:", student[0])
    print("Age:", student[1])
    print("Course:", student[2])
    print()