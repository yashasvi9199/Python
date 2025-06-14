# a --> C   a is parent and c is child
# b --> c   b is parent and c is child


# #1 Parent Class
class Person:
    def p_info(self, name, age):
        print("Inside Person Class")
        print(f"Name : {name}, Age : {age}")


# #2 Parent Class
class Company:
    def l_info(self, company, location):
        print("Inside Company Class")
        print(f"Company name : {company}, Location : {location}")


# Child Class
class Employee(Person, Company):
    def e_info(self, salary, skill):
        print("Inside Child Class")
        print(f"Salary : {salary}, Skill : {skill}")


# Object
emp = Employee()    # No params required since __init__ method is missing

emp.p_info("Yash", 27)
emp.l_info("XYZ Pvt Ltd","Jaipur")
emp.e_info(40000, "Javascript")