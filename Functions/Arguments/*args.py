# Non Key:Value or Keyword arguments


def func(*args):
    for i in args:
        print(i)


def add(*args):
    sum = 0
    for i in args:
        sum += i
    print(sum)


def multiArg(arg, *args):
    print(f"First argument      : {arg}")
    for i in args:
        print(f"Multiple arguments  : {i}")


func("Hello", "Users", "Welcome!")
add(10, 11, 3, 44, 31)
multiArg("First Argument", "Hello", "Users", "Welcome!")
