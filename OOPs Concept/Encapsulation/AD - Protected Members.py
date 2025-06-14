class Company:
    def __init__(self):
        # * Protected Member
        self._project = "JIO MarketPlace"


class Employee:
    def __init__(self, name):
        self.name = name
        Company.__init__(self)  # ? Indirectly writing here whatever is written in Instance method of Company class

    def show(self):
        print(f"Employee name : {self.name}")

        # * Accessing protected member in public method
        print(f"Working on project : {self._project}")


emp = Employee("Yash")  # ? No need to pass project as input as it does not exist in instance parameter of Employee class

print("Accessing Protected member with Public Method")
emp.show()

print()

print("Accessing Protected member directly")
print(f"Project : {emp._project}")
