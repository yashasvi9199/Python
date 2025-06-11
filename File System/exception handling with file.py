try:
    file = open("File.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found") 