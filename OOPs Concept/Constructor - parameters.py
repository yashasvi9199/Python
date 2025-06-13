class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name, self.age)


emp = Employee("Yash", 27)
emp.show()