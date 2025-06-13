class animals:
    # constructor
    def __init__(self, name, age):
        self.name = name  # instance variable
        self.age = age

    #instance method
    def show(self):
        print(f"Animal details : Name : {self.name}, Age : {self.age}")

nos1 = animals("Koala", 40)
nos1.show()

nos2 = animals("Lion", 20)
nos2.show()