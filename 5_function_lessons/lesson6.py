# ==============================
# LAMBDA FUNCTION
# ==============================

# Basic Lambda
square = lambda x: x * x

print("Square:", square(5))


# Multiple Arguments
add = lambda a, b: a + b

print("Addition:", add(10, 20))


# Lambda with Condition
check_age = lambda age: "Adult" if age >= 18 else "Minor"

print("Status:", check_age(20))


# Lambda with max()
products = [
    ("Laptop", 70000),
    ("Phone", 30000),
    ("Tablet", 25000)
]

expensive = max(products, key=lambda product: product[1])

print("Most Expensive:", expensive)


# Lambda with sorted()
students = [
    ("Alex", 85),
    ("Mia", 92),
    ("Sam", 76),
    ("Noah", 88)
]

students_sorted = sorted(
    students,
    key=lambda student: student[1]
)

print("Sorted Students:", students_sorted)


# Lambda with filter()
expenses = [120, 450, 80, 900, 250, 60]

large_expenses = list(
    filter(lambda x: x > 300, expenses)
)

print("Large Expenses:", large_expenses)


# Lambda with map()
numbers = [10, 20, 30, 40]

new_numbers = list(
    map(lambda x: x + 10, numbers)
)

print("New Numbers:", new_numbers)
