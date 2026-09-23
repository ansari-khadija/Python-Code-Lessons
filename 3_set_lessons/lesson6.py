# Set with if, elif and else

subjects = {"Python", "Java", "C++", "HTML"}

subject = input("Enter programming subject: ")

if subject in subjects:
    print("Subject is available")

elif subject == "SQL":
    print("SQL is not in the set")

else:
    print("Subject is not available")