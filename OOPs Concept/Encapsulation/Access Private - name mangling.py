class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary


emp = Employee("Yash", 40000)

try:
    print("Accessing Private member while mangling names :P")
    print("Salary : ", emp._Employee__salary)   #? obj._className__varName

    print("Accessing Private member without using name mangling :(")
    print("Salary : ", emp.__salary)
except:
    print("You cannot access this member, it being private")