# a --> b   'a' is parent class and 'b' is child class

# Parent Class
class Vehicle:
    def v_info(self):
        print("Vehicle Infor from Parent Class")


# Child Class
class Car(Vehicle):
    def c_info(self):
        print("Car info from child class")


new = Car()
new.v_info()
new.c_info()