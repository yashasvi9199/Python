class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary


emp = Employee("Yash", 40000)

try:
    print("Salary : ", emp.salary)
except:
    print("You cannot access this member, it being private")