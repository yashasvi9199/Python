### Using variable value
str = "Yash"
res = f"Name - {str}"           #syntax: f"<new string {variables}"
print(res)              #>>>Name - Yash


### Arithmatic operation
l = 5
b = 3
print(f"Perimeter of rectangle is 2(L+B) = {2*(l+b)}")


### Float Precision
num = 3.14159
print(f"The value of pi is : {num:{1}.{5}}")


### Escape Sequence
a = ord('\n')
print(f"new line : {a}")


### Printing Braces
# Requires 2x braces

print(f"{{HELLO WORLD}}")           # added 2 braces but print 1
print(f"{{{{HELLO WORLD}}}}")       # added 4 braces but print 2

### Printing Dictionaries
# Requires different quotes for key:value

dict = {'Name':'Yash',
'Gender':'Male'}

print(f"Hello {dict['Name']}. You are a {dict['Gender']}")