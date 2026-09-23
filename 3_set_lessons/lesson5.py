# Set with Loops
# Creating a set

subjects = {"Python", "Java", "C++", "HTML", "SQL"}

# 1. Using for loop

print("--- Using for Loop ---")

for subject in subjects:
    print(subject)

# 2. Using for loop with condition

print("\n--- Using if Condition ---")

for subject in subjects:
    if subject == "Python":
        print("Python is present")

# 3. Set of numbers

print("\n--- Numbers in Set ---")

numbers = {10, 20, 30, 40, 50}

total = 0

for number in numbers:
    total = total + number

print("Numbers:", numbers)
print("Total:", total)

# 4. Nested data with loop

print("\n--- Student Names ---")

students = {"Rahul", "Amit", "Priya"}

for student in students:
    print("Student:", student)