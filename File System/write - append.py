with open("File System/testing.txt", "a") as f:
    f.write("\nThis is new content with append functionality")

with open("File System/testing.txt", "r") as f:
    content = f.read()
    print(content)