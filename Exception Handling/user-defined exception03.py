class InvalidAgeError(Exception):
    def __init__(self, age, msg=None):
        
        self.age = age                      #? assigning age to class var if it is an int    

        if msg is None:
            self.msg = "Age must be between 0 and 120"
        else:
            self.msg = msg

        super().__init__(self.msg)

        def __str__(self):
            return f"{self.msg} -> {self.age}"


while (True):
    try:
        age = int(input("Please enter your age : "))
        if age<0 or age>120:
            raise InvalidAgeError(age)
        else:
            print(f"Age set to {age}")
    except InvalidAgeError as e:
        print(e)
    else: 
        break