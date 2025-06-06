class error(Exception):
    """Base class for other exceptions"""

    pass


# * If abve class is not created, it will throw error in below mentioned classes as ;error not defined


class ValueTooSmall(error):
    """Raise when the input value is too small"""

    pass


class ValueTooLarge(error):
    """Raise when the input value is too large"""

    pass


while True:
    try:
        num = int(input("Please enter a number in range 10 to 50: "))
        if num < 10:
            raise ValueTooSmall
        elif num > 50:
            raise ValueTooLarge
        break
    except ValueTooSmall:
        print("Value is too small")
    except ValueTooLarge:
        print("Value is too large")

print(f"You entered {num}")
