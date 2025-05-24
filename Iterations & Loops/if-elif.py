marks = 52

if marks > 90: 
    grade = 'A'
elif marks >80:
    grade = 'B'
else:
    grade = 'C'

print(grade)

### SHORT HAND APPROACH

res = 'a' if marks > 90 else 'b' if marks > 80 else 'c'
print(res)