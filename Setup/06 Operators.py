"""
### 1. Arithmetic Operators
- `+` : Addition
- `-` : Subtraction
- `*` : Multiplication
- `/` : Division (floating-point)
- `//` : Floor Division ()return int value after division by trimming float digits/values
- `%` : Modulus (Remainder)
- `**` : Exponentiation (Power)

### 2. Comparison Operators
- `==` : Equal to
- `!=` : Not equal to
- `>` : Greater than
- `<` : Less than
- `>=` : Greater than or equal to
- `<=` : Less than or equal to

### 3. Logical Operators
- `and` : Logical AND
- `or` : Logical OR
- `not` : Logical NOT

### 4. Assignment Operators
- `=` : Assign
- `+=` : Add and assign
- `-=` : Subtract and assign
- `*=` : Multiply and assign
- `/=` : Divide and assign
- `//=` : Floor divide and assign
- `%=` : Modulus and assign
- `**=` : Exponentiate and assign
"""

a = 45
b= 10

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

print("\n")
      
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

print("\n")
      
print(a>b and a!=b)
print(a>b or a!=b)
print(not(a>b))