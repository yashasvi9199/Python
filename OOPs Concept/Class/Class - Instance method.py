class student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # ? Instance Method
    def show(self):
        print(f"Student details : Name : {self.name}, Age : {self.age}")


s = student("Rahul", 25)
s.show()
