with open("File System/demo.txt", "w") as f:
    f.write("Hello User!!")

# * Reading the file
with open("File System/demo.txt", "r") as f:
    content = f.read()
    print(content)
