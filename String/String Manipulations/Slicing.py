'''
### SYNTAX ###
substring = string[start:end:step]
string          : original string
start(optional) : starting index
end(optional)   : ending index. will be ommitted
step(optional)  : interval b/w indices

return type : str

'''


### Simple Example
str1 = "Hello World"
res = str[0:5]
print(res)              # Hello

### Negative Indexing
str1 = "Hello World"
res = str1[-11:-6]
print(res)              # Hello

### Step
str1 = "Hello World"
res = str1[0:11:2]
print(res)              # HloWr

### Reverse
str1 = "Hello World"
res = str1[::-1]
print(res)              # dlroW olleH

### Get all characters
str1 = "Hello World"
res = str1[:]
res1 = str1[::]
print(res)              # Hello World
print(res1)             # Hello World

### Get all characters before a position
str1 = "Hello World"
res = str1[:5]      # get all chars before 5th index
print(res)              # Hell

### Get all characters after a position
str1 = "Hello World"
res = str1[7:]      # get all chars after 7th index
print(res)              # orld

### Get all characters in a range
str1 = "Hello World"
res = str1[2:7]      # get all chars in range 2 to 7
print(res)              # llo W