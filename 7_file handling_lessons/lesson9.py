f = open("test.txt", "w")
f.write(input("Enter some text: "))
f.close()

f = open("test.txt", "r")
contents = f.read()
f.close()

print(contents)
