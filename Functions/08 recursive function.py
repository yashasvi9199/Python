# A function that keeps on calling itself

def factorial(arg):
    if arg == 0:
        return 1
    else:
        return arg * factorial(arg-1)
    

print(factorial(3))