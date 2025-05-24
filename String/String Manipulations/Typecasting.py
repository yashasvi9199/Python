# Python offer two types of typecasting {changing datatype}
# 1. Explicit Typecasting (performed manually)
# 2. Implicit Typecasting (performed automatically by interpreter)


# 1. Explicit typecasting
a= 1
b= "2"
print(a + int(b))
# using this method we converted the value from string to int.
# Note that it will throw a 'ValueError' error if the values are not as per called function viz, int here.

# 2. Implicit Typecasting
a= 1.2
b= 2
print (a+b)
# Note that answer will be float
# interpreter automtically converted the values to higher datatype to avoid conflict and deliver optimum results