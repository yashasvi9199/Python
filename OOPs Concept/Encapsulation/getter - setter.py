class Employee:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def getAge(self):
        return self.__age

    def setAge(self, age):
        self.__age = age


emp = Employee("Yash", 27)
print(f"Name : {emp.name}, Age: {emp.getAge()}")

emp.setAge(28)

print(f"Updated Age : {emp.getAge()}")