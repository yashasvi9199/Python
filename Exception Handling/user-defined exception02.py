#
# TODO Step 1: Define a custom exception class
class InvalidAgeError(Exception):
    def __init__(self, age, msg="Age must be between 0 and 120"):
        self.age = age
        self.msg = msg
        super().__init__(self, msg)

    def __str__(self):
        return f"{self.msg} -> {self.age}"


#? Exception is passed as param in class and not 'Error'. Exception is base class for all errors already. refere 01
#? __init__ is initialising class attributes
#? self is instance of class to access its var and methods
#? super() is class parent
#? __str__ is another special method like __init__. It returns string representations of class


# TODO Step 2: Use the custom exception class to raise an error
def setAge(age):
    if age < 0 or age > 120:
        raise InvalidAgeError(age)
    else:
        print(f"Age set to {age}")


# TODO Step 3: Handling custom exception
try:
    age = int(input("Please enter your age : "))
    setAge(age)
except InvalidAgeError as e:
    print(e)
