# basic file handling
import os

# Current directory
print("Current Directory:", os.getcwd())

# Create directory
os.mkdir("MyFolder")
print("Directory created")

# Check directory
print("Exists:", os.path.exists("MyFolder"))
print("Is Directory:", os.path.isdir("MyFolder"))

# List contents
print("Contents:", os.listdir("."))

# Change directory
os.chdir("MyFolder")
print("Changed Directory:", os.getcwd())

# Go back
os.chdir("..")

# Rename directory
os.rename("MyFolder", "NewFolder")
print("Directory renamed")

# Remove directory
os.rmdir("NewFolder")
print("Directory removed")
