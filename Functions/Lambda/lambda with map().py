### Map iterates through every item in an iterable such as list, tuple and returns map object
### Syntax ==>>     map( <function> , <iterable>)

listt = [1, 2, 3, 4, 5]
print(listt)

# Normal map()
def sqr(arg):
    return arg**2


res = list(map(sqr, listt))
# print(res)
print(res)


# Lambda map()

sqrt = list(map(lambda arg: arg**0.5    , res))
print(sqrt)