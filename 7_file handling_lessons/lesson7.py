# part_1
with open("sample.txt", "r") as file:
    content = file.read()

print("File Content:")
print(content)

# part_2
with open("sample.txt", "r") as file:
    lines = file.readlines()

# Read last line
print("Last Line:")
print(lines[-1])

# Reverse file content
print("\nReversed Content:")
print("".join(lines)[::-1])
