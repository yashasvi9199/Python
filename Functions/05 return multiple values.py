def ops(a, b):
    add = a+b
    sub = a-b
    multi=a*b
    div = a/b

    return add, sub, multi, div


res1,res2,res3,res4 = ops(10, 2)

print(f"Addition : {res1}")
print(f"Subtraction : {res2}")
print(f"Multiplication : {res3}")
print(f"Division : {res4}")