a = int(input("How many numbers will you enter : "))
listt = []
while a > 0:
    num = float(input("Please enter new number : "))
    listt.append(num)
    a -= 1

listt.sort()
print(f"Maximum number is : {listt[-1]}")