# Conditional Statements
# if, elif and else

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A+")
    print("Excellent performance!")

elif marks >= 80:
    print("Grade: A")
    print("Very good performance!")

elif marks >= 70:
    print("Grade: B")
    print("Good performance!")

elif marks >= 60:
    print("Grade: C")
    print("Keep improving!")

elif marks >= 50:
    print("Grade: D")
    print("You passed!")

else:
    print("Grade: F")
    print("You failed. Better luck next time!")