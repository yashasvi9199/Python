class Employee:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Hello {self.name}"


emp = Employee("Yash")

print(emp)
