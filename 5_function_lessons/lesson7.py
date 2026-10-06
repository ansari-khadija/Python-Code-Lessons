# ==============================
# STUDENT RANKING
# ==============================

students = [
    {"name": "Alex", "math": 85, "science": 90, "english": 78},
    {"name": "Mia", "math": 92, "science": 88, "english": 95},
    {"name": "Sam", "math": 75, "science": 80, "english": 70},
    {"name": "Noah", "math": 88, "science": 91, "english": 84}
]


# Calculate Total
for student in students:
    student["total"] = (
        student["math"]
        + student["science"]
        + student["english"]
    )


# Sort by Total
students = sorted(
    students,
    key=lambda student: student["total"],
    reverse=True
)


# Display Ranking
print("===== STUDENT RANKING =====")

for rank, student in enumerate(students, start=1):
    print(
        rank,
        student["name"],
        "Total:", student["total"]
    )
