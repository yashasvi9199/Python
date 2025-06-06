try:
    a = int(input("Please enter first number : "))
    b = int(input("Please enter second number : "))
    res = a/b
except ValueError as e:
    # throw error in case user enter incorrect type of value (not integer)
    print(f"Error : {e}")
    print("Please enter Integer values only")
except ZeroDivisionError as f:
    print(f"Error : {f}")
    print("Please check the number again")
else : 
    print(f"{a}/{b} = {res}")