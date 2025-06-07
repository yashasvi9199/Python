""" 
try:
    # some code
except:
    # executed if there is an error in try block
else:
    # executed if no error appear
finally:
    # some code... (always executed)
"""

loop1 = True
loop2 = True

while (loop1):
    try:
        a = int(input("Please enter first number : "))
        b = int(input("Please enter second number : "))
        res = a / b

    except ValueError as e:
        print(f"Error : {e}")

    except ZeroDivisionError as f:
        print(f"Error : {f}")

    else:
        print(f"results for {a}/{b} = {res}")

    finally:
        loop2 - True
        while(loop2):
            choice = input("Do you want to coninue (y/n): ")
            match choice:
                case 'y' | 'Y':
                    loop1 = True
                    loop2 = False
#!                     break
                case 'n' | 'N':
                    loop1 = False
                    loop2 = False
#!                     break
#! break
                case _:
                    print("Invalid Input")