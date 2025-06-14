class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def show(self):
        print("Salary : ", self.__salary)


emp = Employee("Yash", 40000)

try:
    print("Accessing Public Class Method")
    emp.show()

    print("Accessing Private member directly with object")
    print("Salary : ", emp.salary)
except:
    print("You cannot access this member, it being private")