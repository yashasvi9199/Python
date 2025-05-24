a = 12
b = True #capital T
c= "Hello"
d= 12.5
e= 12 + 5j

list1 = [1, 2, 3, 4, 5, [10,11,12], ["apple", "mango", "banana"]]       #Lists are mutable and can adapt to changes
tuple1 = (1, 2, 3, 4, 5, [10,11,12], ["apple", "mango", "banana"])   #Tuples are immutable and cannot adapt to changes
# Tuples are immutable, meaning they cannot be changed after creation. Lists are mutable, meaning they can be changed.
# Tuples are faster than lists because they are immutable. Lists are slower than tuples because they are mutable.
# Tuples are used for fixed data, while lists are used for dynamic data.

dict1 = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
# Dictionaries are mutable and can adapt to changes. They are used to store data in key-value pairs.

print(type(a)) # <class 'int'>
print(type(b)) # <class 'bool'>
print(type(c)) # <class 'str'>
print(type(d)) # <class 'float'>
print(type(e)) # <class 'complex'>

print(type(list1)) # <class 'list'>
print (list1)

print(type(tuple1)) # <class 'tuple'>
print (tuple1)

print(type(dict1)) # <class 'dict'>
print (dict1)
