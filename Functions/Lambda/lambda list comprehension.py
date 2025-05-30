# Without List Comprehension
sett = []
for i in range(0, 7):
    sett.append(i)

print(sett)

# List comprehension
# SYNTAX ==>>       <new list> = [<expression> for <variable for loop> in <List variable>]
res = [i**2 for i in sett]
print(res)


# List Comprehension with LAMBDA
sqrt = [lambda args=x: args**0.5 for x in res]
for i in sqrt:
    print(i())
# notice we cannot print the list directly for some reason as it throws lamba functions altogether instead of list


# Alternative to print the above mentioned list
result = [f() for f in sqrt]
print(result)
