#  Used primarily to make a local variable in a function a Global Variable


def outFunc():
    var = 10

    def innerFunc():
        nonlocal var
        var = 99
        print(f"Accessing variable value in inner function: {var}")

    innerFunc()
    print(f"Accessing variable value in outer function: {var}")


outFunc()
# print(f"Accessing variable value outside function: {var}")        This will give error
# Nonlocal can make a local variable global only within functions
