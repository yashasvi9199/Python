class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age


emp = Employee("Yash", 27)
print(f" Name = {emp.name}, Age = {emp.age}")

# ? Used to initialise a data in object of class
# ? Whatever params are passed will directly be accepted in this method/function
