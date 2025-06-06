try:
    a = int(input("Please enter first number : "))
    b = int(input("Please enter second number : "))
    res = a/b
except (ValueError, ZeroDivisionError):
    print("Something went wrong!! \nPlease enter valid numbers")
