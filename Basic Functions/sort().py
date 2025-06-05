# Used to sort iterations
# Syntax ==>> <list var>.sort(reverse=True/False, Key=None, m= None)
# reverse (optional): If True, sorts in descending order; default is False for ascending order.
# key (optional)    : A function for custom sorting conditions.
# m (optional)      : A custom parameter for additional sorting behavior, like a threshold.

num = [12,2,4,1]
print(num)

num.sort()
print(num)

# Descending
num.sort(reverse=True)
print(num)