class Employee:
    count = 0
    def __init__(self):
        Employee.count += 1


emp1 = Employee()
emp2 = Employee()
emp3 = Employee()
emp4 = Employee()
emp5 = Employee()

print("The number of employees : ", Employee.count)