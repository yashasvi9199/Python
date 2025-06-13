class Employee:
    def __init__(self):
        self.name = "Yash"
        self.age = 27

    def show(self):
        print(f"Employee details : Name : {self.name}, Age : {self.age}")


emp = Employee()
emp.show()
