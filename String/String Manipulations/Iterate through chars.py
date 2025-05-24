### Using LOOP
str1 = "Hello Python"

for char in str1:
    print(char)

### Using Enumerate through Index Acess
str1 = "Hello Python"

for i, char in enumerate(str1):
    res = f"Index {i} : {char}"     #formatting with added strings
    print(res)