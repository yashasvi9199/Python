### Simple length of String

str1 = "Hello"
print(len(str1))                            #>>>5

### Length of empty string

str1 = ""
print(len(str1))                            #>>>0

### Length of special characters

str1 = "😄"
print(len(str1))                            #>>>1

### Tuples and Lists

tup = (1,2,3)
lis = [1,2,3,4]

print(len(tup))                            #>>>3
print(len(lis))                            #>>>4

### Dictionary and Sets

dict = {'a':1,'b':2,'c':3}
set1 = {1,2,3,4,5}

print(len(dict))                            #>>>3
print(len(set1))                            #>>>5

### Range

rang = range(0,10)
print(len(rang))                            #>>>10 {0,1,2,3,4,5,6,7,8,9}

### Type Error with len()

# str1 = True
# print(len(str1))                            #>>>TypeError: object of type 'bool' has no len()