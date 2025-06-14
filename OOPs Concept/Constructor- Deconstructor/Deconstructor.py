class Employee:
    def __init__(self, name):
        self.name = name
        print("Inside Constructor")

    def show(self):
        print(f"Hello {self.name}")

    def __del__(self):
        print("Constructor destroyed")


emp = Employee("Yash")  # Inside Constructor
emp.show()  # Hello Yash

# ? Deleting constructor aka Deconstructed
del emp  # Constructor destroyed
