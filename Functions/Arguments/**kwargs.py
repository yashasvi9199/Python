#  kwargs = KeyWordArguments
# They have key=Value parameters

def func1(**kwargs):
    for key,val in kwargs.items():
        print(f"{key} = {val}")


dic = {'Name' : "Yash", "Age":"27"}
# Throws a TypeError as only one argument is given
# func1(dict)

# Throws a SyntaxError as the argument should be Key = Value and not Key:value
# func1('Name' : "Yash", "Age":"27")

func1(name="Yash", sname="Haldiya", age=27)