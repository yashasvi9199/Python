'''
Capitalize the first character of the string
String datatype in Python are immutable 
thus capitalize() returns a new string
we can print is directly as well without a variable
'''

## Case 1 : Simple String with all lower case chars
s = "hello world"
res = s.capitalize()
print(res)      # output >>>Hello world

## Case 2 : Uneven case chars
s = "hELlo WorLD"
res = s.capitalize()
print(res)      # output >>>Hello world

### Case 3 : Numbers in the beginning
s = "123 heLLO WorlD"
res = s.capitalize()
print(res)      # output >>>123 hello world