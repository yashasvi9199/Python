class NegativeAgeError(Exception):
    def __init__(
        self,
        age,
    ):
        message = "Age should not be negaive"
        self.age = age
        self.message = message


age = int(input("Please enter your age : "))
if age < 0:
    raise NegativeAgeError(age)

#TODO This will throw an error. Don't worry about it as the code is working as it is supposed be, which is to raise an error
#TODO The error name shown should be same as the error name defined