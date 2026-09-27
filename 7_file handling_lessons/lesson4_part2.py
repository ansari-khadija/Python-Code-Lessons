import zipfile

# Extract ZIP file
with zipfile.ZipFile("myfiles.zip", "r") as zip_file:
    zip_file.extractall("ExtractedFiles")

print("Files unzipped successfully!")

# Show extracted files
import os

print("Extracted files:")
for file in os.listdir("ExtractedFiles"):
    print(file)
