# ? Syntax ==>> raise ErrorExceptionName("message")


def siCal(amt, year, rate):
    try:
        if amt < 0 or year < 0 or rate < 0:
            raise ValueError("Invalid Input")
        elif rate > 100:
            # raise MyValueError(rate)    # ! This will be incorrect format as 'MyValueError' doesn't exist
            raise ValueError("Interest Rate is out of range")

        res = (amt * year * rate) / 100
        print(f"Simple interest is : {res}")
    except ValueError as e:
        print(f"Error : {e}")
    #! except MyValueError as f:
    #!     print("Interest Rate is out of range", rate)


print("Case 1")
siCal(10000, 10, 12)

print("Case 2")
siCal(-10000, 10, 12)

print("Case 3")
siCal(10000, -10, 12)

print("Case 4")
siCal(10000, 10, -12)

print("Case 5")
siCal(10000, 10, 120)