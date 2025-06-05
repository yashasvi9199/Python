a = int(input("How many numbers would you like to enter : "))
numbers = []
while a > 0:
    inp = float(input(f"Please enter new number : "))
    numbers.append(inp)
    a -= 1  # Decrement


print(f"Sum of numbers is : {sum(numbers)}")
