def dot(func, arg):
    return func(arg)

def square(arg):
    return arg ** 2

def table(arg):
    count = 1
    while count <= 10:
        print(arg * count)
        count += 1
        
    return ''       # if there is no return statement then it will print 'None' (null in python) at the end of functions output

print(dot(square, 3))
print()
print(dot(table, 3))