f = open("File System/testing.txt", "r")
content = f.read(10)     # ? Reading only 10 characters

print(content)
f.close()