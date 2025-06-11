f = open("File System/testing.txt", "r")

print(f)  # ? Printing the object

content = f.read()
print(content)  # ? Printing the content

f.close()