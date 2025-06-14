class Fruits:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def show(self):
        print(f"Fruit details : Name : {self.name}, Color : {self.color}")

obj = Fruits("Apple","Red")

print(obj.show())

del obj.name    # ? delete the object property

print(obj.show())

# ! The whole program will throw error as the original property in method show() has been deleted