f = open("File System/testing.txt", "r")

content = f.readlines()
print(type(content))  # <class 'list'>
print(content)  # ['Hello World\n', 'Welcome to Python tutorials\n', '123 456 789\n']

f.close()


# Reading a file line by line
f = open("File System/testing.txt", "r")

for line in content:
    print(line)

f.close()
