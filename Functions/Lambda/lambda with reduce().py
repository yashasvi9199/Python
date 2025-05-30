### Apply a function throughout the sequence.
### Syntax ==>> reduce( <function> , <iteration>)

from functools import reduce

listt = [1, 2, 3, 4, 5, 6]
print(listt)

# Normal reduce()
def add(a,b):
    return a+b

res = reduce(add, listt)
print(res)

# Lambda reduce()
res = reduce(lambda x,y: x+y   ,listt) 
print(res)