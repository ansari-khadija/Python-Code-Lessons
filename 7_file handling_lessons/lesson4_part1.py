import zipfile

# Create a ZIP file
with zipfile.ZipFile("myfiles.zip", "w") as zip_file:
    zip_file.write("file1.txt")
    zip_file.write("file2.txt")

print("Files zipped successfully!")

# Show files inside ZIP
with zipfile.ZipFile("myfiles.zip", "r") as zip_file:
    print("Files in ZIP:", zip_file.namelist())
