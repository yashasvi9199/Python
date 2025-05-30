# Declaring Global Variable
global_variable = 10

def func1():
    # Calling global variable
    print(f"Accessing Global variable value : {global_variable}")

def func2():
    # Declaring local variable
    local_variable = 5

    # Calling local variable with Global variable
    print(f"Accessing Local variable value : {local_variable}")
    print(f"Accessing Global variable value : {global_variable}")

def func3():
    # Changing values of Global variable w/o Global Keyword
    global_variable = 55

    # Calling Global variable
    print(f"Accessing Global variable value : {global_variable}")

def func4():
    # Checking if Global variable value changed in closed environment of function
    print(f"Accessing Global variable value : {global_variable}")

    # output didn't change the value from 10 to 55

def func5():
    # Changing values for nested function w/o Global Keyword
    global_variable = 66
    fun6()
def fun6():
    print(f"Accessing Global variable value : {global_variable}")
    # No change in values

def func7():
    # Changing values with Global Keyword (declaration method)
    global global_variable
    global_variable = 99
    print(f"Accessing Global variable value : {global_variable}")

def func8():
    print(f"Accessing Global variable value : {global_variable}")
    # Output values permanently changed in above function for global variable

func1()
func2()
func3()
func4()
func5()
func7()
func8()