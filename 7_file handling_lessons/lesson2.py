import os

# Create a folder
os.makedirs("shopping_data", exist_ok=True)

print("Shopping data folder created.")

# Show current directory
print("Current Directory:", os.getcwd())

# Show files and folders
print("\nFiles and Folders:")
print(os.listdir())