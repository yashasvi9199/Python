listItem = ['Hello World\n', 'Welcome to Python tutorials\n', '123 456 789']

#? Writing line by line in file (accepts list as input)
with open("File System/testing.txt", "w") as f:
    f.writelines(listItem)