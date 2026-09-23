#Tuple Methods

subjects = ("Python", "Java", "Python", "C++", "SQL", "Python")
print("Subjects:", subjects)

#count() method
print("\n--- count() Method ---")
print("Python appears:", subjects.count("Python"), "times")
print("Java appears:", subjects.count("Java"), "time")

#index() method
print("\n--- index() Method ---")
print("First occurrence of Python:", subjects.index("Python"))
print("Position of Java:", subjects.index("Java"))
print("Position of SQL:", subjects.index("SQL"))

#len() function
print("\n--- len() Function ---")
print("Number of subjects:", len(subjects))

#Accessing elements using indexing
print("\n--- Indexing ---")
print("First subject:", subjects[0])
print("Third subject:", subjects[2])
print("Last subject:", subjects[5])

#Slicing
print("\n--- Slicing ---")
print("First three subjects:", subjects[0:3])
print("Last three subjects:", subjects[3:6])