# Advanced file handling
import os
import shutil
from pathlib import Path

# Create nested directories
os.makedirs("Parent/Child", exist_ok=True)

# Check path
path = Path("Parent/Child")

print("Exists:", path.exists())
print("Is Directory:", path.is_dir())

# List directory
print("Contents:", list(path.iterdir()))

# Create a file
file = path / "example.txt"
file.write_text("Hello Python!")

print("File created:", file)

# Check file
print("Is File:", file.is_file())

# Remove file
file.unlink()
print("File removed")

# Remove complete directory
shutil.rmtree("Parent")
print("Directory removed")
