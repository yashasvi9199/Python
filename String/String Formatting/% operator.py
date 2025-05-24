'''
%s - String datatype
%r - raw datatype
%d - Integer datatype <need prior declaration using typecasting int()>
%f - Float datatype <need prior declaration using typecasting int()/ float()>
%c - char  datatype <need prior declaration using typecasting int()/ or char data in '<single char>'>
%x - Hexadecimal datatype
%o - Octal datatype
'''

var = '15'

str = "Variable as String = %s" %(var)
print(str)

str = "Variable as Raw = %r" %(var)
print(str)

var = int(var)      #typecasting for numeral values

str = "Variable as Integer = %d \n\
Variable as Float = %5.3f" %(var,var)   # %5.3f is a format specifier. Meaning total of 5 digits where 3 digits are after decimal results 00.000
print(str)


str = "Variable as Char = %c \n\
Variable as Hexadecimal = %x \n\
Variable as Octal = %o" %(var,var,var)
print(str)


### AS OBJECTS OF A CLASS

class Person:
    def __str__ (self):
        return "Person Object"

obj = Person()      # OOPS concept
message = "The object is : %s" % obj

print(message)