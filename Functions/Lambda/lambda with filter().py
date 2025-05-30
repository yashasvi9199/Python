### Check if elements in a sequence are true or false (on condition)
# Syntax ==>>   filter( <function>, <sequence>)


# Normal filter()
def even(arg):
    return arg % 2 == 0


listt = [1, 2, 3, 4, 5, 6, 7, 8, 9]
out = filter(even, listt)
res = list(out)  # Converting object to list
print(res)


# Lambda filter()

listt = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even = filter(lambda arg: arg%2==0  ,  listt)
print(list(even))