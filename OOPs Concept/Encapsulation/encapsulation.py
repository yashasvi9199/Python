class Employee:
    def __init__(self, name, project, salary):
        #* Data members
        self.name = name
        self.project = project
        self.salary = salary

        #* method
    def show(self):
        print(f"Name : {self.name}, Salary : {self.salary}")

    #* method
    def post(self):
        print(f"Name : {self.name}, Project : {self.project}")


emp1 = Employee("Yash", "JIO Marketplace", 25000)

emp1.show()
emp1.post()