import re

# Define a string
text = "The quick brown fox jumps over the lazy dog."

# Use regex to find and replace the word 'fox' with 'cat'
new_text = re.sub('fox', 'cat', text)

# Print the original and new strings
print("Original text:", text)
print("New text:", new_text)
