class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print("Accessing Class method")
        print (f"Name : {self.name}, Salary : {self.salary}")


emp = Employee("Yash", 40000)
emp.show()

print("Accessing public members of class")
print(f"Name = {emp.name}, Salary = {emp.salary}")