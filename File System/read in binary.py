file1 = open("File System/testing.txt", "rb")
content1 = file1.read()
print(content1)     # b'Hello World\nWelcome to Python tutorials\n123 456 789'

file2 = open("File System/test.png", "rb")
content2 = file1.read()
print(content2)     # Error nothing is printed

file1.close()
file2.close()