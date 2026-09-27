# counting file handling
# part_1
with open("sample.txt", "r") as file:
    text = file.read()

# Count numbers
numbers = sum(char.isdigit() for char in text)

# Count characters
characters = len(text)

print("Number of digits:", numbers)
print("Total characters:", characters)


# part_2
word = input("Enter word to search: ")

with open("sample.txt", "r") as file:
    text = file.read()

count = text.lower().count(word.lower())

print("Word:", word)
print("Total occurrences:", count)
