# Tuple Indexing POSITIVE

subjects = ("Python", "Java", "C++", "SQL", "HTML")
print("Subjects:", subjects)

# Accessing elements using positive indexing
print("\n--- Tuple Indexing ---")
print("First subject:", subjects[0])
print("Second subject:", subjects[1])
print("Third subject:", subjects[2])
print("Fourth subject:", subjects[3])
print("Fifth subject:", subjects[4])

# Finding the length of tuple
print("\nNumber of subjects:", len(subjects))

# Accessing an element using a variable
index = int(input("\nEnter an index (0-4): "))
print("Subject at index", index, ":", subjects[index])
