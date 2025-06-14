# ? There are two attributes in python class :
# ? Instance Variable and Class Variable


class student:
    # class variable
    school_name = "ABCD Public School"

    # Constructor
    def __init__(self, name, age):
        # instance variable
        self.name = name
        self.age = age


stud1 = student("Yash", 27)  # ?using object
print(f"Student : {stud1.name}, {stud1.age}")
print(f"School Name : {student.school_name}")  # ?using class


stud2 = student("Yashasvi", 27)  # ?using object
print(f"Student : {stud2.name}, {stud2.age}")
student.school_name = "XYZ Public School"  # ? accessing class variable
print(f"School Name : {student.school_name}")
