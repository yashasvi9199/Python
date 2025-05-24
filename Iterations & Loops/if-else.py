age = int(input("Please enter your age : "))

if age >= 18:
    print("You can vote!")
else:
    print("You cannot vote!")

## SHORT HAND APPROACH
# ADDING VALUES IN A VARIABLE

res = "Congratulations!" if age >=18 else "Try again later!"
print(res)