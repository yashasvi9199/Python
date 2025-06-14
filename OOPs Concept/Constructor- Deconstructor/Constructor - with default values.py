class Employee:

    def __init__(self, name, age, post="Software Engineer"):
        self.name =name
        self.age = age
        self.post = post

    def show(self):
        print(f"Employee details : Name : {self.name}, Age : {self.age}, Post : {self.post}")


emp1 = Employee("Yash", 27)
emp1.show()

emp2 = Employee("Yashasvi", 27, "Manager")
emp2.show()