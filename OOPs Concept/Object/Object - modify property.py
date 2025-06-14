class Fruits:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def show(self):
        print(f"Fruit details : Name : {self.name}, Color : {self.color}")


obj = Fruits("Apple","Red")

print(obj.show())

obj.name = "Strawberry"

print(obj.show())