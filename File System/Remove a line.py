with open("File System/testing.txt", "r") as f:
    content = f.readlines()  # ? Creating a list to be operated

# ? removing specific item in list {Check options to remove items in list}
content.remove("123 456 789")

with open("File System/testing.txt", "w") as f:
    f.writelines(content)  # ? writing the file with updated 'content'

with open("File System/testing.txt", "r") as f:
    contentRead = f.read()  # ? Reading the file again
    print(contentRead)


# TODO Recreating the index in file
content.append("123 456 789")
with open("File System/testing.txt", "w") as f:
    f.writelines(content)
