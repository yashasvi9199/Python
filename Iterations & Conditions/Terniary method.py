### if-else
# var=  <value if true> |if condition| |else| <value if false>
age = 15
res = "Congratulations!" if age >=18 else "Try again later!"
print(res)


### if-else nested
# var = value_if_true if condition else value_if_false
marks = 53
res = 'a' if marks > 90 else 'b' if marks > 80 else 'c'
print(res)

### Tuple
# var = condition_is_false, condition_is_true)[condition]
n = 7
res = ("Odd","Even") [n%2 == 0]
print(res)

### Dictionary
# dict = {True: value_if_true, False: value_if_false} [Condition]
a= 10
b= 20
max = {True:a, False:b} [a > b]
print(max)